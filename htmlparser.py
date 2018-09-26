from abstractparser import AbstractParser
from bs4 import BeautifulSoup


class HTMLParser(AbstractParser):

    links = []

    def parse(self, path_to_document):
        parser = 'html.parser'
        soup = BeautifulSoup(open(path_to_document, 'rb').read(), parser)
        self.text = soup.get_text()
        for link in soup.find_all('a'):
            self.links.append((link.get_text(), link['href']))

    def get_links(self):
        return self.links
