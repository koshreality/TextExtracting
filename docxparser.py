import docx2txt
from abstractparser import AbstractParser


class DocxParser(AbstractParser):

    def parse(self, path_to_document):
        self.text = docx2txt.process(path_to_document)
