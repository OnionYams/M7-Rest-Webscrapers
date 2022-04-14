import dataclasses
from dataclasses import dataclass

@dataclass
class Elixirs:
    id: str
    Name: str  
    Difficulty: str
    Ingredient: str
    InventorFullName: None
    Manufacturer: None
    effect: str
    sideEffects: None
    characteristics: None

@dataclass
class Houses:
    id: str
    Name: str
    HouseColours: str
    Founder: str
    Animal:	str
    Element: str
    Ghost: str
    CommonRoom:	str

@dataclass
class Ingredients:
    id: str
    Name: str  

@dataclass
class Spells:
    id: str
    Name: str  
    Type: str
    Incantation: str

@dataclass
class Wizards:
    id: str
    FirstName: str  
    LastName: str



from bs4 import BeautifulSoup
import requests
import json

def getHTML(url):
    response = requests.get(url)
    return response.text


responseIngre = requests.get("https://wizard-world-api.herokuapp.com/Ingredients")
#print(dir(responseIngre))

ingres = responseIngre.json()
#print(blah)
ingredientList = []
for i in ingres:
   ingredientList.append(Ingredients(i["id"], i["name"]))
   
#print(ingredientList)
#print(ingres[0].keys())

responseElix = requests.get("https://wizard-world-api.herokuapp.com/Elixirs")
#print(dir(responseElix))

elixs = responseElix.json()
#print(blah)
#print(elixs[0].keys())
elixirList = []
for i in elixs:
   elixirList.append(Elixirs(i["id"], i["name"], i["difficulty"], i["ingredients"], i["inventors"], i["manufacturer"],
                            i["effect"], i["sideEffects"], i["characteristics"]))
   

#print(elixirList)


#with open("text.json", "w") as f:
    #json.dumps(list(elixirList))

'''
html = getHTML("https://wizard-world-api.herokuapp.com/Elixirs")

soup = BeautifulSoup(html,'html.parser')
table = soup.find('li',attrs = {'class':'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
rawrows = []
filledRow = []
'''


