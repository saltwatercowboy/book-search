from PyPDF2 import PdfFileReader
import re
import csv
from itertools import zip_longest

#searches through pdf book and adds page numbers to lists
def text_search(pdf_file):
    with open(pdf_file, 'rb') as f:
        pdf = PdfFileReader(f)
        numpages = pdf.getNumPages()
        global queries1
        queries1 = []
        global queries2
        queries2 = []
        global queries3
        queries3 = []
        #search functions in regex are a little unpythonic but work for now
        for i in range (0, numpages):
            page = pdf.getPage(i)
            pagetext = page.extractText()
            if re.search(r'\bcat\b', pagetext):
                query1 = pdf.getPageNumber(page)
                print('Query 1 found on page {}'.format(query1))
                query1str = str(query1)
                queries1.append(query1str)
                print(queries1)
            
            elif re.search(r'\bcats\b', pagetext):
                query2 = pdf.getPageNumber(page)
                print('Query 1 found on page {}'.format(query2))
                query2str = str(query2)
                queries1.append(query2str)
                print(queries1)
                
            elif re.search(r'\bear\b', pagetext):
                query3 = pdf.getPageNumber(page)
                print('Query 2 found on page {}'.format(query3))
                query3str = str(query3)
                queries2.append(query3str)
                print(queries2)
                
            elif re.search(r'\bears\b', pagetext):
                query4 = pdf.getPageNumber(page)
                print('Query 2 found on page {}'.format(query4))
                query4str = str(query4)
                queries2.append(query4str)
                print(queries2)
                
            elif re.search(r'\bCutty Sark\b', pagetext):
                query5 = pdf.getPageNumber(page)
                print('Query 3 found on page {}'.format(query5))
                query5str = str(query5)
                queries3.append(query5str)
                print(queries3)            

#joins lists, zips them with itertools and writes to a .csv
def writer():
    rows = [queries1, queries2, queries3]
    data = zip_longest(*rows, fillvalue='') 
    with open('cats.csv', 'w+', newline='') as f:
        query_writer = csv.writer(f)
        query_writer.writerow(('Cat(s)', 'Ear(s)', 'Cutty Sark'))
        query_writer.writerows(data)
                
if __name__ == '__main__':
    pdf_file = 'The Wind-Up Bird Chronicle.pdf'
    text_search(pdf_file)
    writer()
