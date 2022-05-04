import scrapy
from collections import Counter
import re
import numpy as np
from operator import itemgetter
import operator

#with scrapy i can extract the data from the url given html
class News(scrapy.Spider):
    name = 'news'
    start_urls = ['https://news.ycombinator.com/']

    def parse(self, response):
        table = response.css('.itemlist')
        i = 0
        np.array_result = []
        for entrie in table.xpath('tr'):
          if i == 0:
            title = entrie.css('.titlelink').xpath('text()').get()
            number = entrie.css('.rank').xpath('text()').get()

            if title is None:
              break
            i += 1
          elif i == 1:
            #Getting the filters
            i += 1
            array_details = entrie.css('.subtext').xpath('span/text()').getall()            
            if len(array_details) > 0:
               text = array_details[0]
               score = int(text[0: len(text) - len('score') - 1])              
            else:
               score = 0
            text_a = entrie.css('.subtext').xpath('a/text()').getall()[-1]            
            if 'comments' in text_a:
               comments = int(text_a[0:len(text_a) - len('comments')-1])
            else:
               comments = 0            
          else: 
            i = 0            
            np.array_result.append([number, title, len(re.findall(r'\w+', title)), score, comments])

        arr = np.array_result
        
        #Showing the results
        print("==================================WEBCRAWLER================================== ")
        
        print("**The first 30 news** ")
        for first30 in arr:
            print(first30, "\n")

        print("==================================FILTERS================================== ")        
        print ("\n ** The entries with more than five words in the title and ordered by comments ** \n")
        
        #•	Filter all previous entries with more than five words in the title ordered by the number of comments first.
        
        firstfilter =  sorted(filter(lambda a: a[2] > 5, arr), key=itemgetter(4), reverse= True)
        for filterone in firstfilter:
            print(filterone, "\n")

        print ("\n ** The entries with less or equal to five words in the title and ordered by points ** \n")  

        #•	Filter all previous entries with less than or equal to five words in the title ordered by points.
        
        secondfilter =  sorted(filter(lambda a: a[2] <= 5, arr), key = operator.itemgetter(3), reverse = True)
        for filtertwo in secondfilter:
            print(filtertwo, "\n")