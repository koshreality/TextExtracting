from pdfparser import PDFParser
from docxparser import DocxParser


def pdf_test():
    pdf_parser = PDFParser()
    pdf_parser.parse(r'D:\Test.pdf')
    print(pdf_parser.get_processed_stems())


def docx_test():
    docx_parser = DocxParser()
    docx_parser.parse(r'D:\Test.docx')
    print(docx_parser.get_processed_stems())


if __name__ == '__main__':
    # pdf_test()
    docx_test()
