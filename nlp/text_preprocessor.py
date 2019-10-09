import re

class TextPreprocessor:
    """
    A util-class for preprocessing texts.
    It has ability to modify texts like removal of blank records.
    The list of texts which are supposed to be preprocessed are to be specified
    as the argument of the constructor.
    After calling methods for preprocess, the result can be accessed by the attribute "result".
    """

    def __init__(self, text_list):
        """
        Constructor

        Parameters
        ----------
        text_list : list of str
            The list of texts to be preprocessed.
        """
        self.result = text_list

    def remove_blanks(self):
        """
        Remove blank texts.
        """
        self.result = [text for text in self.result if text]

    def remove_by_regexes(self, regexes):
        """
        Remove words matching given regular expressions.

        Parameters
        ----------
        regexes : list of str
            The list of regexes to be used for the removal.
        """
        for regex in regexes:
            self.result = [text for text in self.result if re.match(regex, text) is None]

