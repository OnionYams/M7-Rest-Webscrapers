from lib2to3.pgen2.token import RARROW
from bs4 import BeautifulSoup
import requests

def getHTML(url):
    response = requests.get(url)
    return response.text


response = requests.get("http://books.toscrape.com/")
print(response)

html = getHTML("http://books.toscrape.com/")

soup = BeautifulSoup(html,'html.parser')
table = soup.find('li',attrs = {'class':'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
rawrows = []
filledRow = []
#print(table)

#find all next to get main attribute
# . to get subattribute, ie .a for anchor, .p for paragraph
# .string for text that displays, ie black text between html tags
# [] for indexing, 
for row in table.find_all_next('article'):
    #divs = row.find_all_next('div')
    nameCells = row.find_all_next("h3")
    bookDicts = {}
    #rawrows.append(cells[0].string)
    #print(cells[0].string)

    starCell = row.find_all_next("p")
    #print(cell2[0]["class"][1])

    priceCell = row.find_all_next("div")
    #print(cell3[1])
    #print(priceCell[1].p.string)

    #[1:] to exclude random special char before euro
    bookDicts['name'] = nameCells[0].a["title"]
    bookDicts['stars'] = starCell[0]["class"][1]
    bookDicts['price'] = priceCell[1].p.string[1:]
    filledRow.append(bookDicts)
    
    #stars = row.find_all_next("p")
    #print(stars)
    #starrow.append(stars[0].string)

for bruh in filledRow:
    print(bruh)

import csv

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'stars', "price"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for dict in filledRow:
        writer.writerow(dict)
#print(rawrows[0], rawrows[1], rawrows[2])
#print(starrow[0], starrow[1], starrow[2])