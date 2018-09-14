import PyPDF2
import gensim.parsing.preprocessing as prep


class PDFParser:

    text = ""

    def parse(self, path_to_document):

        pdf = PyPDF2.PdfFileReader(open(path_to_document, 'rb'))
        num_pages = pdf.getNumPages()

        for i in range(num_pages):
            self.text += pdf.getPage(i).extractText()

    def get_text(self):
        return self.text

    def get_words(self):
        return self.text.split()

    def get_stems(self):
        return prep.stem(self.text).split()

    def get_processed_text(self):
        return prep.remove_stopwords(prep.strip_non_alphanum(self.text))

    def get_processed_stems(self):
        return prep.stem(prep.remove_stopwords(prep.strip_non_alphanum(self.text))).split()
