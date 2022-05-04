import scrapy
from collections import Counter
import requests
import re
import string
import numpy as np
from operator import itemgetter
import operator

#with scrapy i can extract the data from the url given html
class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://news.ycombinator.com/']

    def parse(self, response):
        table = response.css('.itemlist')
        i = 0
        np.array_result = []
        for row in table.xpath('tr'):
          if i == 0:
#extract the notice title
            title = row.css('.titlelink').xpath('text()').get()
            number = row.css('.rank').xpath('text()').get()

            if title is None:
              break
            i += 1
          elif i == 1:
#extract the notice points
            i += 1
            array_span = row.css('.subtext').xpath('span/text()').getall()            
            if len(array_span) > 0:
               text = array_span[0]
               points = int(text[0: len(text) - len('points') - 1])              
            else:
               points = 0
#extract the number of comments
            text_a = row.css('.subtext').xpath('a/text()').getall()[-1]            
            if 'comments' in text_a:
               comments = int(text_a[0:len(text_a) - len('comments')-1])
            else:
               comments = 0            
          else: 
            i = 0            
            np.array_result.append([number, title, len(re.findall(r'\w+', title)), points, comments])

        arr = np.array_result
        
#printing the numpy array that contains the 30 articles on web
        
        print("The First 30 Articles are : ")
        for first30 in arr:
            print(first30, "\n")

        print ("\n \n Now the entries with more than five words in the title and ordered by comments are: \n \n")
        
#Filter all previous entries with more than five words in the title ordered by the number of comments first.
        
        firstfilter =  sorted(filter(lambda a: a[2] > 5, arr), key=itemgetter(4), reverse= True)
        for filterone in firstfilter:
            print(filterone, "\n")

        print ("\n \n now the entries with less or equal to five words in the title and ordered by point are: \n \n")
        
#Filter all previous entries with less than or equal to five words in the title ordered by points.
        
        secondfilter =  sorted(filter(lambda a: a[2] <= 5, arr), key = operator.itemgetter(3), reverse = True)
        for filtertwo in secondfilter:
            print(filtertwo, "\n")