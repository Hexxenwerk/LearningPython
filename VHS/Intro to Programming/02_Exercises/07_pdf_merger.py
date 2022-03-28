import os

from PyPDF2 import PdfFileMerger


def merge_pdf():
    pdf_list = ['/'.join([os.getenv('HOME'), 'f1.pdf']), '/'.join([os.getenv('HOME'), 'f2.pdf']),
                '/'.join([os.getenv('HOME'), 'f3.pdf']), '/'.join([os.getenv('HOME'), 'f4.pdf'])]
    print(pdf_list)
    merger = PdfFileMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    merger.write(os.getenv('HOME') + '/result.pdf')
    print('Successfully saved')


def main():
    merge_pdf()


if __name__ == '__main__':
    main()
