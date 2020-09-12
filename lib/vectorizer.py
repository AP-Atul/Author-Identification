"""
This class read the data and converts them into
numbers using marathi vowels and consonant and
other unique letters
"""


class Vectorizer:
    def __init__(self, wordSize=5):
        self.wordSize = wordSize  # feature that satisfies the word size
        self.consonants = ['क', 'ख', 'ग', 'घ', 'ङ',
                           'च', 'छ', 'ज', 'झ', 'ञ',
                           'ट', 'ठ', 'ड', 'ढ', 'ण',
                           'त', 'थ', 'द', 'ध', 'न',
                           'प', 'फ', 'ब', 'भ', 'म',
                           'य', 'र', 'ल', 'व', 'श',
                           'ष', 'स', 'ह', 'ळ', 'क्ष', 'ज्ञ']
        self.vowels = ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ऋ', 'ए', 'ऐ', 'ओ', 'औ', 'अं', 'अः']
        self.matras = ['ऀ', 'ँ', 'ं', 'ः', 'ऺ', 'ऻ', '़', 'ऽ', 'ा', 'ि', 'ी', 'ु', 'ू', 'ृ',
                       'ॄ', 'ॅ', 'ॆ', 'े', 'ै', 'ॉ', 'ॊ', 'ो', 'ौ', '्', 'ॎ', 'ॏ', '॑',
                       '॒', '॓', '॔', 'ॕ', 'ॖ', 'ॗ', 'ॢ', 'ॣ']
        self.virams = ['.', ';', '‘', ',', '?', '!', '”', '—', '–', '/', ':']

    def transform(self, article):
        """
        article should be output of file read lines
        read line by line and create the feature vector
        :param article: lol, list of list of file
        :return: list, list of all features
        """
        totalConsonants = 0
        totalVowels = 0
        totalMatras = 0
        totalWordSize = 0
        noOfLines = 0
        noOfChars = 0
        noOfWords = 0
        noOfWordsPerSize = 0
        noOfWordsBelowSize = 0
        noOfWordsAboveSize = 0

        for line in article:
            words = line.split(" ")
            noOfLines += 1
            noOfWords += len(words)
            for word in words:
                totalWordSize += len(word)
                if len(word) < self.wordSize:
                    noOfWordsBelowSize += 1
                elif len(word) == self.wordSize:
                    noOfWordsPerSize += 1
                else:
                    noOfWordsAboveSize += 1

                for char in word:
                    noOfChars += 1
                    if char in self.consonants:
                        totalConsonants += 1
                    elif char in self.vowels:
                        totalVowels += 1
                    elif char in self.matras:
                        totalMatras += 1

        avgWordSize = totalWordSize / noOfWords
        noOfVowelsPerWord = totalVowels / noOfWords
        noOfConsonantsPerWord = totalConsonants / noOfWords
        noOfMatrasPerWord = totalMatras / noOfWords

        # following features are returned
        return [noOfLines,
                noOfChars,
                noOfWords,
                avgWordSize,
                noOfVowelsPerWord,
                noOfConsonantsPerWord,
                noOfMatrasPerWord,
                noOfWordsPerSize,
                noOfWordsBelowSize,
                noOfWordsAboveSize]
