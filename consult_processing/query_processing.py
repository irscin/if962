from nltk.corpus import stopwords 
import re
import unidecode
import os
import operator
import json
from math import log
from sklearn.feature_extraction.text import TfidfVectorizer

class GeneralQuery:
    def __init__(self, queryString, description, OS, ram, storage, price, useTfIdf = True):
        self.queryString = queryString
        self.description = description
        self.OS = OS
        self.ram = ram
        self.storage = storage
        self.price = price
        self.documents = os.path.abspath('../inverted_index/db/')
        self.twoTermsPath = os.path.abspath('../inverted_index/twoTerms.json')
        self.invIndexPath = os.path.abspath('../inverted_index/frequency.json')
        self.fieldQuery = QueryProcessor(invIndexPath=self.twoTermsPath, documentsPath=self.documents)
        self.wordQuery = QueryProcessor(invIndexPath=self.invIndexPath, documentsPath=self.documents)
        self.useTfIdf = useTfIdf

    def processQuery(self):
        gameList = []
        if(self.queryString != ''):
            games = self.wordQuery.query(self.queryString, useTfIdf = self.useTfIdf)
            gameList.append(games)
        if(self.description != ''):
            games = self.fieldQuery.query(self.description, useTfIdf=self.useTfIdf, field="description")
            gameList.append(games)
        if(self.storage != ''):
            games = self.fieldQuery.query(self.storage, useTfIdf=self.useTfIdf, field="storage")
            gameList.append(games)
        if(self.OS != ''):
            games = self.fieldQuery.query(self.OS, useTfIdf=self.useTfIdf, field="os")
            gameList.append(games)
        if(self.price != ''):
            games = self.fieldQuery.query(self.price, useTfIdf=self.useTfIdf, field="price")
            gameList.append(games)
        if(self.ram != ''):
            games = self.fieldQuery.query(self.ram, useTfIdf=self.useTfIdf, field="ram")
            gameList.append(games)
        
        gamesHash = {}
        #take average of the tfidf of each game returned in the query
        for i in range(len(gameList)): 
            for game in gameList[i]:
                if not str(game[0]) in gamesHash:
                    gamesHash[str(game[0])] = float(game[1])
                else:
                    gamesHash[str(game[0])] += float(game[1])
    
        for name in gamesHash:
            gamesHash[name] /= 6

        #sort by highest tfidf average
        sorted_games = sorted(gamesHash.items(), key=operator.itemgetter(1), reverse=True)

        return sorted_games

class QueryProcessor():
    def __init__(self, invIndexPath, documentsPath):
        self.descr = None
        self.queryTerms = None
        self.invIndex = None # inverted index file
        self.posting = None # posting file (document at a time)
        self.termIDF = None
        self.lengthDoc = None
        self.documentsPath = documentsPath
        self.setInvIndex(invIndexPath)
        self.wordsDocuments = list(self.invIndex.keys()) # all words of all documents
        self.numDocs = len(os.listdir(documentsPath)) # number of documents in database
        self.setLengthDocs() # set length of documents
        self.runIDF()
        
    '''
        * Method where receive an list of words and cleans it, removing
        * stopwords (if useStopwords == True), accentuation and punctuation
    '''
    def cleaning(self, words, field, useStopwords = False):
        if type(words) == str:
            substr = re.findall(r'"(.*?)"', words)
            words = re.sub(r'"(.*?)"', '', words)
            words = words.strip().split(' ')
            words = words + substr
        toRemove = r'[.*,;\(\)\'\"\?\!%\$]'
        for i in range(len(words)):
            words[i] = re.sub(toRemove, '', words[i])
            words[i] = unidecode.unidecode(words[i])
        if useStopwords:
            set_sw = set(stopwords.words('english'))
            newWords = []
            for word in words:
                if not word in set_sw:
                    if(field):
                        newWords.append(word + '.' + field)
                    else:
                        newWords.append(word)
            return list(set(newWords))
        if(field):
            for i in range(len(words)):
                words[i] = words[i] + '.' + field
        return list(set(words))
            
    '''
        * Set the self.invIndex to a dict where key is a term and values is a tuple
        * (freq, doc), where freq is the frequency of that key term in the document
        * doc
    '''
    def setInvIndex(self, path):
        with open(path, encoding='unicode_escape') as file:
            file_text = file.read()[2:-1]
            json_dict = json.loads(file_text)
        self.invIndex = json_dict
    
    '''
        *Runs the term at a time algorithm and set self.posting with a dictionary 
        *with scores of all documents by frequency of terms
    '''
    def readPosting(self, queryWords):
        localReadPosting = {}
        for term in queryWords:
            freqDocList = self.invIndex.get(term, None)
            if freqDocList:
                for freq, doc in freqDocList:
                    localReadPosting[doc] = localReadPosting.get(doc, 0) + freq
        self.documentTermFrequency = localReadPosting
        
    def getPosting(self):
        return self.posting
            
    '''
        * TF algorithm returns the term frequency in a document. An different approach is divide
        * this frequency by the number of words in a document
    '''
    def runTF(self, term, document):
        for freq, doc in self.invIndex[term]:
            if doc == document:
                return freq
        return 0
    
    
    '''
        * IDF algorithm computes the importance of a term calculating the log of the division between the number
        * of documents by the number of documents that contains a term. 
    '''
    def runIDF(self):
        termIDF = {}
        for term in self.invIndex.keys():
            numDocsByTerm = len(self.invIndex[term])
            #print(numDocsByTerm)
            idf = log(self.numDocs/numDocsByTerm)
            termIDF[term] = idf
        self.termIDF = termIDF
                
            
    def setQuery(self, queryString, field):
        cleanQuery = self.cleaning(queryString, field, useStopwords=True)
        self.readPosting(cleanQuery)
        self.queryTerms = cleanQuery
        
    def performQuery(self, useTfIdf):
        score = {i: 0 for i in range(1,self.numDocs+1)}
        for term in self.queryTerms:
            invIndexValues = self.invIndex.get(term, False)
            if not invIndexValues:
                continue
            for freq, doc in self.invIndex[term]:
                auxScore = freq
                if useTfIdf:
                    auxScore = auxScore*self.termIDF.get(term, 0)
                score[doc] += auxScore
        for doc in score:
            score[doc] = score[doc]/self.lengthDoc[doc]
        score = sorted(score.items(), key = lambda x : x[1], reverse=True)
        return score[:11]
    
    
    def query(self, queryString, useTfIdf = False, field = None):
        self.setQuery(queryString, field)
        return self.performQuery(useTfIdf)
    
            
    def setLengthDocs(self):
        lengthDoc = {}
        for fileName in os.listdir(self.documentsPath):
            filePath = self.documentsPath + '/' + fileName
            #print(filePath)
            with open(filePath, 'r') as fp:
                lengthDoc[int(fileName)] = len(fp.read().split(' '))
        self.lengthDoc = lengthDoc

# %%
invIndexPath = os.path.abspath('../inverted_index/frequency.json')
twoTermsPath = os.path.abspath('../inverted_index/twoTerms.json')
documents = os.path.abspath('../inverted_index/db/')

# %%
qp = QueryProcessor(invIndexPath=invIndexPath, documentsPath=documents)

# %%
rankingTFIDF = dict(qp.query('dark souls', useTfIdf=True))
rankingTFIDF

# %%
ranking = dict(qp.query('dark souls', useTfIdf=False))
ranking

# %%
numDocs = len(list(ranking.keys())+list(rankingTFIDF.keys()))

# %%
def getSumSquareDist(r1, r2):
    result = 0
    docs = list(r1.keys())+list(r2.keys())
    for doc in docs:
        squareDistance = (r1.get(doc, 0)-r2.get(doc,0))**2
        result += squareDistance
    return result

# %%
sumSquareDistance = getSumSquareDist(rankingTFIDF, ranking)

# %%
def spearmanCorrelation(sumSquareDist, k):
    num = 6*sumSquareDist
    den = k*(k**2-1)
    return 1-(num/den)

# %%
spearmanCorrelation(sumSquareDistance, k = numDocs)

# %%
def comparissonSpearmanCorrelation(queries, numDocs):
    for q in queries:
        ranking = dict(qp.query(q))
        rankingTFIDF = dict(qp.query(q, useTfIdf= True))
        sumSquareDistance = getSumSquareDist(rankingTFIDF, ranking)
        sc = spearmanCorrelation(sumSquareDistance, k = numDocs)
        print("Query #(" + q + "):")
        #print("Sum Square Distance = %.2f"%(sumSquareDistance))
        print("Spearman = %f"%(sc))
        #print(sc)

# %%
comparissonSpearmanCorrelation(['"dorfromantik"', "hollow knight", "maquette", "little nightmares II", "windows 2gb ram"], numDocs)

# %%
a = dict(qp.query('windows 2gb ram', useTfIdf=False))
b = dict(qp.query('windows 2gb ram', useTfIdf=True))

# %%
getSumSquareDist(a, b)

# %%
b

# %%
queryTFIDF = GeneralQuery("hollow knight", '', 'windows', '', '', '', useTfIdf=False)
rankAtributeTFIDF = dict(queryTFIDF.processQuery())
print("Sem TFIDF: " + '.'.join(str(x) for x in queryTFIDF.processQuery()))

# %%
query = GeneralQuery("hollow knight", '', 'windows', '', '', '', useTfIdf=True)
rankAtribute = dict(query.processQuery())
print("Com TFIDF: " + '.'.join(str(x) for x in query.processQuery()))

# %%
sumSquareDistance = getSumSquareDist(rankAtributeTFIDF, rankAtribute)

# %%
numDocs = len(list(rankAtribute.keys())+list(rankAtributeTFIDF.keys()))
spearmanCorrelation(sumSquareDistance, k = numDocs)