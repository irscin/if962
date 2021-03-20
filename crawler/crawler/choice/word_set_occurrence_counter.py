class WordSetOccurrenceCounter:
    def __init__(self, word_set=set()):
        self.word_set = word_set

    def count_occurrences(self, phrase):
        words = self.words_from(phrase)
        return sum([1 for word in words if word in self.word_set])

    def words_from(self, phrase):
        return phrase.split(' ')
