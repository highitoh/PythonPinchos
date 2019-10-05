import pandas as pd
import xml.etree.ElementTree as ET
import re
import os

class MemberCommentAnalyzer:
    """
    Analyzer of comments which are described in the members of classes.
    It analyzes XML format files that Doxygen outputs.
    """

    COMPOUND_NAME_COLUMN_NAME = 'compound_name'
    MEMBER_NAME_COLUMN_NAME = 'member_name'
    COMMENT_COLUMN_NAME = 'comment'
    TEXT_DF_COLUMNS = [COMPOUND_NAME_COLUMN_NAME, MEMBER_NAME_COLUMN_NAME, COMMENT_COLUMN_NAME]

    def __init__(self, filename_list):
        """
        Constructor

        Parameters
        ----------
        filename_list : list of str
            The list of The names of XML files to be analyzed.
        """
        self.result = {}
        self.filename_list = filename_list

    def analyze(self):
        """
        Analyze comments from the XML files specified in the filename list.
        """
        for filename in self.filename_list:
            tree = ET.parse(filename)
            compounddefs = tree.findall('./compounddef')
            self.result.update(self.__get_compounddefs_comment_dict(compounddefs))

    def __get_compounddefs_comment_dict(self, compounddefs):
        compound_member_comment_dict = {}
        for compounddef in compounddefs:
            compound_name = compounddef.find('compoundname').text
            memberdefs = compounddef.findall('./sectiondef/memberdef')
            member_comment_dict = self.__get_memberdefs_comment_dict(memberdefs)
            compound_member_comment_dict[compound_name] = member_comment_dict
        return compound_member_comment_dict

    def __get_memberdefs_comment_dict(self, memberdefs):
        member_comment_dict = {}
        for memberdef in memberdefs:
            member_name = memberdef.find('name').text
            description = memberdef.find('detaileddescription')
            para_text = ''
            for para in description.iter('para'):
                if type(para.text) == str:
                    para_text = para_text + para.text
            member_comment_dict[member_name] = para_text
        return member_comment_dict

    def get_dataframe(self):
        """
        Get analyzed comments by a dataframe.

        returns
        -------
        DataFrame
            A dataframe which contains analyzed comments.
        """
        df = pd.DataFrame(columns=self.TEXT_DF_COLUMNS)

        for compound_name in self.result.keys():
            member_comment_dict = self.result[compound_name]
            for member_name in member_comment_dict:
                comment = member_comment_dict[member_name]
                s = pd.Series([compound_name, member_name, comment], index=df.columns)
                df = df.append(s, ignore_index=True)
        return df
