"""
DESCRIPTION: Search for a song by entering the name of an artist. The program returns the song title and
artist name and also gives the user an option of would they like to see the lyrics
to the song as well.
In addition, the user can also get more information of the artist by an URL, which will lead the user to a profile page.

AUTHORS: Paul Sining Lu

LAST UPDATE: 04/22/22

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
        self.artistObj = None

    def search(self):
        """
        Description: This function prints out the top 5 songs 
        based on the Artists entered in by the user.
        Parameters: None
        Return: None
        """
        # top results in dictionary form prouduced from lyrics entered by the user
        try:
            results_artist = self.genius_object.search_artist(
                self.artist, max_songs=5, sort='popularity')
            self.artistObj = results_artist
        except:
            print(
                "Something went wrong... Please enter a valid artist name or check your internet and try again.")

    def getArtist(self):
        """
        Description: This function prints out the Artist info and 
        generate an url for more details about the artist entered in by the user.
        Parameters: None
        Returns: The Artist Name for the song entered in by the user and the url link to the artist page. 
        """
        if self.artistObj is None:
            print("Please enter the valid artist name first ...")
            return

        print(f"The artist name is {self.artistObj.name}")
        print(f"You can find more details in this url: \n{self.artistObj.url}")

    # override
    def __str__(self):
        return f"This is the Artist Search Box, and the Artist you entered are: {self.artist}"
