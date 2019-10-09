import re
import numpy as np
from collections import Counter

class TokenPreprocessor:
    """
    A util-class for preprocessing tokens created by the morphological_analyzer.
    It has ability to modify words like removal of stopwords.
    The list of tokens which are supposed to be preprocessed are to be specified
    as the argument of the constructor.
    After calling methods for preprocess, the result can be accessed by the attribute "result".
    """

    def __init__(self, tokenized_list):
        """
        Constructor

        Parameters
        ----------
        tokenized_list : list of list of tokens
            The list of tokens to be preprocessed.
            The parameter can be obtained by the morphological_analyser.analyze() method.
        """
        self.result = tokenized_list

    def get_words(self):
        """
        Get words by string as the result of preprocesses.

        Returns
        -------
        word_list : list of list of str
            The list of words created from preprocessed tokens.
        """
        word_list = [[token.surface for token in sentence] for sentence in self.result]
        return word_list

    def remove_blanks(self):
        """
        Remove blank words in given tokens.
        """
        self.result = [[token for token in sentence if token.surface] for sentence in self.result]

    def remove_stopword(self, stopwords):
        """
        Remove stopwords in given tokens.

        Parameters
        ----------
        stopwords : list of str
            The list of words to be removed from tokens. (stopwords)
        """
        for stopword in stopwords:
            self.result = [[token for token in sentence if stopword != token.surface]
                                 for sentence in self.result]

    def remove_by_regexes(self, regexes):
        """
        Remove words matching given regular expressions.

        Parameters
        ----------
        regexes : list of str
            The list of regexes to be used for the removal.
        """
        for regex in regexes:
            self.result = [[token for token in sentence if re.match(regex, token.surface) is None]
                                for sentence in self.result]

    def remove_frequent_words(self, threshold=100):
        """
        Remove frequent words in given tokens.
        The words which has top-(threshold) occurence will be removed.

        Parameters
        ----------
        threshold : int
            The threshold for removal.
        """
        words_list = []
        for sentence in self.result:
            words = []
            for token in sentence:
                words.append(token.surface)
            words_list.append(words)

        # Get frequent words and remove them
        frequent_words = self.__get_frequent_words(words_list, threshold)
        self.result = [[token for token in sentence if token.surface not in frequent_words]
                              for sentence in self.result]

    def __get_frequent_words(self, words_list, threshold):
        fdist = Counter()
        for words in words_list:
            for word in words:
                fdist[word] += 1
        common_words = {word for word, freq in fdist.most_common(threshold)}
        return common_words

