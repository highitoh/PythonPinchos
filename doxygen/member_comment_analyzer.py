import pandas as pd
import xml.etree.ElementTree as ET
import glob
import re
import os

class MemberCommentAnalyzer:

    def __init__(self, path):
        self.path = path

    def analyze(self):
        xml_file_names = glob.glob(self.path)
        self.result = {}

        for xml_file_name in xml_file_names:
            tree = ET.parse(xml_file_name)
            compounddefs = tree.findall('./compounddef')
            self.result.update(self.__get_compounddefs_comment_dict(compounddefs))

    def get_dataframe(self):
        df = pd.DataFrame(columns=['compound_name', 'member_name', 'comment'])

        for compound_name in self.result.keys():
            member_comment_dict = self.result[compound_name]
            for member_name in member_comment_dict:
                comment = member_comment_dict[member_name]
                s = pd.Series([compound_name, member_name, comment], index=df.columns)
                df = df.append(s, ignore_index=True)
        return df

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


