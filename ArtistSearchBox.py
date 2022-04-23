"""
DESCRIPTION:

AUTHORS: Paul Sining Lu

LAST UPDATE:

Class Variables: 
1. genius_access_token -> str(allows access to genius API)
2. genius_object -> instantiation of genius object which allows access
to methods of the genius API.

Functions: 
1. search()
2. getArtist()
3. __str__()


"""
# imported libraries
import lyricsgenius as lg
from searchBox import SearchBox


class ArtistSearchBox(SearchBox):

    genius_access_token = "_rDAy259SoA7baRL1ouy2MWdOADsdevMvTvMxo83XXtJJ-ejmfSNvtZSrbqJZrvZ"
    genius_object = lg.Genius(genius_access_token)

    def __init__(self, artist: str) -> None:
        self.artist = artist

    def search(self):
        pass

    def getArtist(self):
        pass

    # override
    def __str__(self):
        pass
