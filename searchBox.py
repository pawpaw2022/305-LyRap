"""
DESCRIPTION: SearchBox is a abstract superclass which provides a 
blueprint for subsequent sublclasses that inherit its functionality.

AUTHORS: Paul Sining Lu, Grace Gresli, Aidan Pearce, Bruce Tukuafu

LAST UPDATE: 04/22/22
    
Functions:
1. search() 
2. getLyrics()
3. getArtist()
4. getTitle()
5. __str__() 
"""
# imported libraries
from abc import abstractmethod

class SearchBox(object):
    def __init__(self, name:str) -> None:
        self.name = name

    @abstractmethod
    def search(self, keyword:str): 
        pass
        
    @abstractmethod
    def getLyrics(self, keyword:str):
        pass
    
    @abstractmethod
    def getArtist(self, keyword:str):
        pass

    @abstractmethod
    def getTitle(self, keyword:str) -> str:
        pass

    def __str__(self) -> str:
        return f" This is a General Search Box, and the phrase you entered is {self.name}"

