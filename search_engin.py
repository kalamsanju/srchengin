#!/usr/bin/python

##### This script use inverted index of 10000 web pages pages its location is
##### var/www/html/cgi-bin folder and webpages are stored in /home/crawled data/webpages files  
##### and indexed files created in /home/crawled data/online_search

# Import modules for CGI handling
import cgi
import cgitb
cgitb.enable()

#Create instance of FieldStorage
form = cgi.FieldStorage()

print "Content-Type: text/html\n\r\n\r"
print '<html>'
print '<head><title>Search Page</title></head>\n\n'
print '<body>'
print '<p>Search Results !!! </p>' 

#Get data from fields
q = form.getvalue('query_term')

# python search script
index_dir = "indexing"
####for web hosting path selection shuold be like this
#####index_dir = "/public_html/indexing/"
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from bs4 import BeautifulSoup


def main():
    list1 = {}
    #q = raw_input('Enter Event to search:')
    ix = open_dir(index_dir)
   
    with ix.searcher() as searcher:
        
        query = QueryParser("content", schema = ix.schema).parse(unicode(q))
        results = searcher.search(query, limit= 20)
        #results = searcher.search(query)
        print '<div style="color:red">'
        print '<h4>'
        print ('Documents matched--', len(results), 'for the query = ' + q )
        print '</h4>'
        print '<p>Showing results...</p>'
        print '</div>'
        if len(results) != 0:
            for res in results:
                try:
                   if res['title'] is not None:
                    #print '<div style="color:#006621">'
                      print '<a href='+ res['path'] +'/>'
                      print '<br>' 
                      print res['title'] + ' <br> ' + '<div style="color:#006621">' +  res['path']
                      
                      print res['path']
                      print '</div>'
                      #print '<br>'
                except:
                      pass
        else:
            print ("No documents found for the given query " + q)


if __name__ == '__main__':
    main()

print '</form>'


print '</body>'
print '</html>'


