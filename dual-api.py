from dataclasses import dataclass
import dataclasses
from datetime import datetime
from pickle import STOP
from turtle import title
import requests
import json

@dataclass
class Film:
    title: str
    episodeid: int
    crawl: str
    chars: list
    rating: float
    #earned: None
   # def __ge_____:

    def findEP(self, epnum):
        if self.episodeid == epnum:
            return f"{self.title} is episode {epnum}"

@ dataclass
class Character:
    name: str
    #height: float
    #gender: str

@dataclass
class Library:
    movies: list

    def findEP(self, epnum):
        for film in self.movies:
            if film.episodeid == epnum:
                return f"{film.title} is episode {epnum}"


def getHTML(url):
    response = requests.get(url)
    return response.text


#omep4 = requests.get("http://www.omdbapi.com/?t=star+wars+a+new+hope&year=1977&plot=full&apikey=960ccee7")
#omep4 = requests.get("http://www.omdbapi.com/?apikey=960ccee7&t=star+wars&year=1980").json()

#print(omep4)

#print(dir(omep4))
#print(omep4json.items())

ep4 = requests.get("https://swapi.dev/api/films")

#print(dir(ep4))
ep4json = ep4.json()
#print(ep4json.keys())
#print(ep4.text)
lib = Library([])
#print(ep4json["results"][0]["characters"])

years = [1977,1980,1983]
print("start")
psuedoindex = 0
for i in ep4json["results"]:
    #print(i)
#print(type(ep4json))
    charList = []
    loops = 0
    for j in ep4json["results"][psuedoindex]["characters"]:
        char = requests.get(j).json()
        
        charList.append(Character(char["name"]))
        loops += 1
        if loops > 5:
            break

    omep = requests.get("http://www.omdbapi.com/?apikey=960ccee7&t=star+wars&year=" + str(years[psuedoindex])).json()

    lib.movies.append(Film(i["title"], i["episode_id"], i["opening_crawl"], charList, omep["imdbRating"] ))

    psuedoindex += 1
    if psuedoindex >= 3:
        break
    #for j in omep4json:
    #break
#print(filmList)

print(lib.movies)


omep4 = requests.get("https://swapi.dev/api/people")

omep4json = omep4.json()

blah = int(input("episode to search for: "))

'''for i in lib.movies:

    print(i.findEP(blah) if 1.findEP(blah) != None else "")'''
print(lib.findEP(blah))

#for i in omep4json["results"]:
    #print(i["name"])
print("done")

if __name__ == "__main__" :
    print("allo")