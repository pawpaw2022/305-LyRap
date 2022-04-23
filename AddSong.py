"""
DESCRIPTION:

AUTHORS: Aidan Pearce

LAST UPDATE:

Class Variables: 
1. genius_access_token -> str(allows access to genius API)
2. genius_object -> instantiation of genius object which allows access
to methods of the genius API.

Functions:
1. getName()
2. getLyrics()
3. getArtist()
4. getYear()
5. __str__()

"""
import lyricsgenius as lg
from abc import override

class ArtistSearchBox(object):
    
    genius_access_token = "_rDAy259SoA7baRL1ouy2MWdOADsdevMvTvMxo83XXtJJ-ejmfSNvtZSrbqJZrvZ"
    genius_object = lg.Genius(genius_access_token)

    def __init__(self, name:str, lyrics:str, artist:str, year:str) -> None:
        self.name = name
        self.lyrics = lyrics
        self.artist = artist
        self.year = year

    def getName(self):
        pass
    def getLyrics(self):
        pass
    def getArtist(self):
        pass
    def getYear(self):
        pass
    def __str__(self):
        pass