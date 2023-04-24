from PyPDF2 import PdfReader, PdfWriter
import argparse

"""
usage: add_watermark_in_pdf.py [-h] [-o Target] Source Watermark

source file path and watermark file path

positional arguments:
  Source      source file path
  Watermark   watermark file path

options:
  -h, --help  show this help message and exit
  -o Target   out put file path
"""

def add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out) -> None:
    pdf_output = PdfWriter()
    input_stream = open(pdf_file_in, 'rb')
    pdf_input = PdfReader(input_stream, strict=False)

    pdf_watermark = PdfReader(open(pdf_file_mark, 'rb'), strict=False).pages[0]
    
    for page in pdf_input.pages:
        page.merge_page(pdf_watermark)
        page.compress_content_streams()
        pdf_output.add_page(page)
        
    pdf_output.write(open(pdf_file_out, 'wb'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='source file path and watermark file path')
    parser.add_argument(
        dest='pdf_file_in', metavar='Source', type=str, 
        help='source file path'
    )
    parser.add_argument(
        dest='pdf_file_mark', metavar='Watermark', type=str,
        help='watermark file path'
    )
    parser.add_argument(
        '-o', dest='pdf_file_out', default='./a.pdf', metavar='Target', type=str,
        help='out put file path (defalut: ./a.pdf)'
    )
    
    args = parser.parse_args()
    add_watermark(args.pdf_file_in, args.pdf_file_mark, args.pdf_file_out)
    