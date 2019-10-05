import pandas as pd
from docx import Document

class DocxTextAnalyzer:
    """
    Analyzer of texts from the word file(.docx).
    It uses python-docx package.
    """

    FILENAME_COLUMN_NAME = 'filename'
    STYLE_COLUMN_NAME = 'style'
    TEXT_COLUMN_NAME = 'text'
    TEXT_DF_COLUMNS = [FILENAME_COLUMN_NAME, STYLE_COLUMN_NAME, TEXT_COLUMN_NAME]

    def __init__(self, filename_list):
        """
        Constructor

        Parameters
        ----------
        filename_list : list of str
            The list of The names of word files(.docx) to be analyzed.
        """
        self.result = {}
        self.filename_list = filename_list

    def analyze(self):
        """
        Analyze texts from the word files(.docx) specified in the filename list.

        Notes
        -----
        This method uses python-docx package.
        """
        self.result.clear()
        self.result[self.FILENAME_COLUMN_NAME] = []
        self.result[self.STYLE_COLUMN_NAME] = []
        self.result[self.TEXT_COLUMN_NAME] = []

        for filename in self.filename_list:
            self.__analyze_single_file(filename)

    def __analyze_single_file(self, filename):
        style_list = []
        text_list = []

        document = Document(filename)
        for paragraph in document.paragraphs:
            style = paragraph.style.name
            text = paragraph.text.strip()
            if text:    # ignore a blank text
                style_list.append(style)
                text_list.append(text)
        filename_list = [filename] * len(text_list)

        self.result[self.FILENAME_COLUMN_NAME].extend(filename_list)
        self.result[self.STYLE_COLUMN_NAME].extend(style_list)
        self.result[self.TEXT_COLUMN_NAME].extend(text_list)


    def get_dataframe(self):
        """
        Get analyzed texts by a dataframe.

        returns
        -------
        DataFrame
            A dataframe which contains analyzed texts.
        """
        df = pd.DataFrame(data=self.result, columns=self.TEXT_DF_COLUMNS)
        return df

