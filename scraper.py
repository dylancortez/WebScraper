#import data scraping libraries
import requests
from bs4 import BeautifulSoup

#This program is an attempt to scrape information from the web and turn it into a dataset.
#This program will take information from Barnes and Noble's book selection and give us information on books, their prices, and their ratings.

webpage = requests.get("https://www.barnesandnoble.com/b/books/_/N-29Z8q8")
soup = BeautifulSoup(webpage.content, "html.parser")

print(webpage.content)
