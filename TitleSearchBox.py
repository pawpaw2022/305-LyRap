"""
DESCRIPTION:

AUTHORS: Grace Gresli

LAST UPDATE:

Class Variables: 
1. genius_access_token -> str(allows access to genius API)
2. genius_object -> instantiation of genius object which allows access
to methods of the genius API.

Functions: 
1. search()
2. getTitle()
3. __str__()

"""
# imported libraries
import lyricsgenius as lg
from SearchBox import SearchBox


class TitleSearchBox(SearchBox):

    genius_access_token = "_rDAy259SoA7baRL1ouy2MWdOADsdevMvTvMxo83XXtJJ-ejmfSNvtZSrbqJZrvZ"
    genius_object = lg.Genius(genius_access_token)

    def __init__(self, title: str) -> None:
        self.title = title

    def search(self):
        pass

    def getTitle(self):
        pass

    # override
    def __str__(self):
        pass
