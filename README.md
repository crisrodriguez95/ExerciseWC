# ExerciseWC
Using the language that you feel most proficient in, you’ll have to create a web crawler using scraping techniques to extract the first 30 entries from https://news.ycombinator.com/ . You’ll only care about the title, the number of the order, the number of comments, and points for each entry. <br>

From there, we want it to be able to perform a couple of filtering operations:<br>
•	Filter all previous entries with more than five words in the title ordered by the number of comments first.<br>
•	Filter all previous entries with less than or equal to five words in the title ordered by points.<br>

## Using pip it is mandatory to install scrapy and numpy
- pip install scrapy<br>
- pip install numpy
## Change the path to the root of the project and execute this comand
- python -m scrapy runspider news.py

## Then scroll up to part that has the results
![image](https://user-images.githubusercontent.com/62897412/166621537-edafd4f4-4fc2-42e3-a798-62169dbbc794.png)




