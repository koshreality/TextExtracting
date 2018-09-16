import PyPDF2
from abstractparser import AbstractParser


class PDFParser(AbstractParser):

    def parse(self, path_to_document):

        pdf = PyPDF2.PdfFileReader(open(path_to_document, 'rb'))
        num_pages = pdf.getNumPages()

        for i in range(num_pages):
            self.text += pdf.getPage(i).extractText()
