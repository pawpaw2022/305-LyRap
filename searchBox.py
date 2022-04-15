'''
SearchBox is a superclass that contains: 
    dataField: 
    1. name: str
    2. result: list of dict
        [{
            artist: Dua Lipa
            songName: 
            Lyric: 
        }, ...
        ]
    function:
    1. search() 
    2. getResult()
    3. getName()
    4. setName()
    5. __str__() 
'''
from abc import abstractmethod
import json_test

class SearchBox(object):
    def __init__(self, name:str) -> None:
        self.name = name
        self.result = []
        self.criteria = "DEFAULT" # title, lyrics, artist.
        
    @abstractmethod
    def search(self, keyword:str) -> list: 
        for song in json_test.song_db: 
            if keyword in song[self.criteria]:
                self.result.append(f"{song['title']} - {song['artist']}")
                return "Result has been found !!!"
    
        return "No result matched."
        

    def getResult(self) -> list:
        return self.result

    def getName(self) -> str:
        return self.name

    def setName(self,name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f" This is a {self.criteria} search Box, its name is {self.getName()}, currently it has found {len(self.result)} results."

