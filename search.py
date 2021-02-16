from PyPDF2 import PdfFileReader
import re
import csv

def text_search(pdf_file):
    with open(pdf_file, 'rb') as f:
        pdf = PdfFileReader(f)
        numpages = pdf.getNumPages()
        global queries1
        queries1 = []
        global queries2
        queries2 = []
        
        for i in range (0, numpages):
            page = pdf.getPage(i)
            pagetext = page.extractText()
            if re.search(myRegex, pagetext):
                query1 = pdf.getPageNumber(page)
                print('Query 1 found on page {}'.format(query1))
                query1str = str(query1)
                queries1.append(query1str)
                print(queries1)
            
            elif re.search(myRegexplural, pagetext):
                query2 = pdf.getPageNumber(page)
                print('Query 2 found on page {}'.format(query2))
                query2str = str(query2)
                queries2.append(query2str)
                print(queries2)
            
def writer():
    with open('Mentions.csv', 'a', newline='') as f:
        query_writer = csv.writer(f)
        #query_writer.writerow(['Page Number'] + ['Book'] + ['Query'])
        for query in queries1:
            query_writer.writerow([query] + [bookname] + [search])
        for query in queries2:
            query_writer.writerow([query] + [bookname] + [search])
        
                
if __name__ == '__main__':
    search = 'cat'
    bookname = 'Norwegian Wood'  
    pdf_file = 'Norwegian Wood.pdf'    
    myRegex = r'\b' + search + r'\b'
    myRegexplural = r'\b' + search + 's' + r'\b'
    text_search(pdf_file)
    writer()
