from pdfparser import PDFParser
from docxparser import DocxParser
from docoleparser import DocOleParser
from docconverterparser import DocConverterParser
from htmlparser import HTMLParser


def pdf_test():
    pdf_parser = PDFParser()
    pdf_parser.parse(r'D:\Test.pdf')
    print(pdf_parser.get_processed_stems())


def docx_test():
    docx_parser = DocxParser()
    docx_parser.parse(r'D:\Test.docx')
    print(docx_parser.get_processed_stems())


def doc_ole_test():
    doc_parser = DocOleParser()
    doc_parser.parse(r'D:\Test.doc')
    print(doc_parser.get_processed_stems())


def doc_converter_test():
    doc_parser = DocConverterParser()
    doc_parser.parse(r'D:\Test.doc')
    print(doc_parser.get_processed_stems())


def html_test():
    html_parser = HTMLParser()
    html_parser.parse(r'D:\Test2.html')
    print(html_parser.get_processed_stems())
    print(html_parser.get_links())


if __name__ == '__main__':
    # pdf_test()
    # docx_test()
    # doc_ole_test() # not working
    # doc_converter_test()
    html_test()
