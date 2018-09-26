import win32com.client
from abstractparser import AbstractParser
import docx2txt


class DocConverterParser(AbstractParser):

    def parse(self, path_to_document):
        wrd = win32com.client.Dispatch("Word.Application")
        wrd.Visible = False
        path_without_extension = ''.join(path_to_document.split('.')[0:-1])
        wb = wrd.Documents.Open(path_to_document)
        wb.SaveAs(path_without_extension + '_converted.docx', FileFormat=16)
        wb.Close()
        wrd.Quit()
        self.text = docx2txt.process(path_without_extension + '_converted.docx')
