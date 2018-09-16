from abc import ABC, abstractmethod
import gensim.parsing.preprocessing as prep


class AbstractParser(ABC):

    text = ""

    @abstractmethod
    def parse(self, path_to_document):
        pass

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
