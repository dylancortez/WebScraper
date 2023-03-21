#import data scraping libraries
import requests
from bs4 import BeautifulSoup
import csv

#This program is an attempt to scrape information from the web and turn it into a dataset.
#This program will take information from Scraping Sandbox, a free-to-access website designed to practice web scraping tools
url = "http://books.toscrape.com/catalogue/page-1.html"
#print("created the url")
response = requests.get(url)
print("got the response object")
soup = BeautifulSoup(response.content, "html.parser")
#print("created the soup object")
#Find the information we want to extract from the HTML content
data = [["Book Title", "Price"]]
product_list = soup.find_all('li', {'class': 'col-xs-6'})
#print("created the list and object!")
#Find each individual product on the page and information on each product using HTML tags
for product in product_list:
    name = product.find('h3').text.strip()
    price = product.find('p', {'class': 'price_color'}).text.strip()
    data.append([name, price]) #Add scraped data to data list
    #print("found and added the data!")

#Write the data into a CSV file
filename = 'data.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Done scraping!")
