#!/usr/bin/env python
# coding: utf-8

# In[128]:


import os
import re
import json
from sklearn.feature_extraction.text import CountVectorizer
from nltk import ngrams


# In[133]:


vectorizer = CountVectorizer(ngram_range=(1,2))


# In[134]:


def frequencyDocument(json_dict, file_index):
    w = []
    for words in json_dict.values():
        if words in ['', '--', ' ', '.', ' -']:
            continue
        w.append(words)

    matrix = []
    try:
        matrix = vectorizer.fit_transform(w).toarray()
    except:
        return
    matrix = matrix.sum(axis = 0)

    for word, index in vectorizer.vocabulary_.items():
        freqDoc = (int(matrix[index]), int(file_index))
        if not inv_index_frequency.get(word, False):
            inv_index_frequency[word] = set()
        inv_index_frequency[word].add(freqDoc)


# In[175]:


def twoTermsDocument(json_dict, file_index):
    for key, words in json_dict.items():
        if words in ['', '--', ' ', '.', ' -']:
            continue
        if(words):
            words = words.strip().split(' ')
            words = words + [' '.join(t) for t in ngrams(words, 2)]
            diff_words = set()
            for word in words:
                cont = 0
                if word in ['', '--', ' ', '.', '-', ',']:
                    continue
                for word2 in words:
                    if(word == word2):
                        cont += 1
                if not word in diff_words:
                    freqDoc = (cont, word)
                    diff_words.add(freqDoc)
                else:
                    continue
            for freq, word in diff_words:        
                newKey = word + '.' + key
                freqDoc = (int(freq), int(file_index))
                if not inv_index_twoTermsDocs.get(newKey, False):
                    inv_index_twoTermsDocs[newKey] = set()
                inv_index_twoTermsDocs[newKey].add(freqDoc)


# In[176]:


inv_index_frequency = {}
inv_index_twoTermsDocs = {}
path_db = os.path.abspath('./db')
for file_name in os.listdir(path_db):
    file_path = path_db + '/' + file_name
    with open(file_path, 'r', encoding='utf-8') as file:
        file_text = file.read()
        file_text = re.sub(r'\\xc2|\\xae|\\xe2|\\x80|\\x99|\\x84|\\xa2|\\x93|\\xa0|\\', '', file_text)
        json_dict = json.loads(file_text[:-1])
    frequencyDocument(json_dict, file_name)
    twoTermsDocument(json_dict, file_name)


# In[177]:


for key in inv_index_frequency.keys():
    inv_index_frequency[key] = sorted(inv_index_frequency[key], key = lambda val: val[1])


# In[179]:


for key in inv_index_twoTermsDocs.keys():
    inv_index_twoTermsDocs[key] = sorted(inv_index_twoTermsDocs[key], key = lambda val: val[1])


# In[181]:


def saveJSON(dict_file, filename):
    with open(filename, 'w', encoding='utf-8') as fp:
        json_text = json.dumps(dict_file, ensure_ascii=False).encode('utf-8')
        fp.write(str(json_text))


# In[182]:


saveJSON(inv_index_frequency, 'frequency.json')
saveJSON(inv_index_twoTermsDocs, 'twoTerms.json')


# In[183]:


print('Size of file Frequency: %.2f kB'%(os.path.getsize('frequency.json')/1024.0))
print('Size of file TwoTerms: %.2f kB'%(os.path.getsize('twoTerms.json')/1024.0))


# In[184]:


for key in inv_index_twoTermsDocs:
    for i in range(len(inv_index_twoTermsDocs[key])-1, 0, -1):
        freqDoc = (inv_index_twoTermsDocs[key][i][0], inv_index_twoTermsDocs[key][i][1]-inv_index_twoTermsDocs[key][i-1][1])
        inv_index_twoTermsDocs[key][i] = freqDoc


# In[185]:


saveJSON(inv_index_twoTermsDocs, 'twoTermsCompressed.json')


# In[186]:


for key in inv_index_frequency:
    for i in range(len(inv_index_frequency[key])-1, 0, -1):
        freqDoc = (inv_index_frequency[key][i][0], inv_index_frequency[key][i][1]-inv_index_frequency[key][i-1][1])
        inv_index_frequency[key][i] = freqDoc


# In[149]:


saveJSON(inv_index_frequency, 'frequencyCompressed.json')


# In[188]:


print('Size of file Frequency Compressed: %.2f kB'%(os.path.getsize('frequencyCompressed.json')/1024.0))
print('Size of file TwoTerms Compressed: %.2f kB'%(os.path.getsize('twoTermsCompressed.json')/1024.0))


# In[196]:


# In[ ]:




