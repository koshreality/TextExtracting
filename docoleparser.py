from abstractparser import AbstractParser
import olefile


class DocOleParser(AbstractParser):

    def parse(self, path_to_document):
        ole = olefile.OleFileIO(path_to_document)
        if ole.exists('WordDocument'):
            document = ole.openstream('WordDocument')
            self.text = document.read().decode(errors='ignore')
        ole.close()
