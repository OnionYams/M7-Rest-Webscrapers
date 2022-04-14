import dataclasses
from dataclasses import dataclass

@dataclass
class Elixirs:
    id: str
    Name: str  
    Difficulty: str
    Ingredient: str
    InventorFullName: str
    Manufacturer: str

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