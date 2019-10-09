from janome.tokenizer import Tokenizer

class MorphologicalAnalyzer:
    """
    A class which conducts morphological analysis for given texts.
    The morphological analysis uses the janome library which is for japanese texts.
    https://mocobeta.github.io/janome/en/
    """

    def __init__(self, text_list):
        """
        Constructor

        Parameters
        ----------
        text_list : list of str
            The list of texts which is the target of a morphological analysis.
        """
        self.text_list = text_list
        self.result = None

    def analyze(self, udic_file_name=None, udic_type='ipadic'):
        """
        Do morphological analysis with the janome package.

        Parameters
        ----------
        udic_file_name : str, default None
            The file name of the user dictionary which will be used in morphological analysis.
        udic_type: str, default 'ipadic'
            The type of the user dicionary which is written by.
            This is indicated by the types defined in janome's Tokenizer constructer.
            The detail is shown in the janome's documentation.

        Returns
        -------
        tokenized_list : list of list of token
            The result of morphological analysis.
            The tokens which is list of token are inserted to the list by each sentense.

        Notes
        -----
        This method uses janome package.
        """
        if user_dict_file_name is None:
            # Create tokenizer without a user dictionary
            t = Tokenizer()
        else:
            # Create tokenizer with a user dictionary
            t = Tokenizer(udic_file_name, udic_type=udic_type)

        # Do morphological analysis
        tokenized_list = []
        for text in self.text_list:
            tokens = t.tokenize(text)
            if len(tokens) > 0:
                tokenized_list.append(tokens)
        self.result = tokenized_list
       
