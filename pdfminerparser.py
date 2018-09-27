from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from abstractparser import AbstractParser


class PDFMinerParser(AbstractParser):

    def parse(self, path_to_document):
        rsrcmgr = PDFResourceManager()
        sio = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        fp = open(path_to_document, 'rb')
        for page in PDFPage.get_pages(fp):
            interpreter.process_page(page)
        fp.close()

        self.text = sio.getvalue()

        device.close()
        sio.close()
