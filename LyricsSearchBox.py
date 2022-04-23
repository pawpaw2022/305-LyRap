"""
DESCRIPTION: LyricSearchBox is a subclass of SearchBox and allows
the user to search for a song based on lyrics entered into the search box.
The results will produce the top 10 results when searching the database for a
song with the specified lyrics.

AUTHORS: Bruce Tukuafu

LAST UPDATE: 04/14/22

Class Variables: 
1. genius_access_token -> str(allows access to genius API)
2. genius_object -> instantiation of genius object which allows access
to methods of the genius API.

Functions: 
1. search()
2. getLyrics()
3. setLyrics()
4. __str__()
"""
# imported libraries
import lyricsgenius as lg
from searchBox import SearchBox


class LyricsSearchBox(SearchBox):

    genius_access_token = "_rDAy259SoA7baRL1ouy2MWdOADsdevMvTvMxo83XXtJJ-ejmfSNvtZSrbqJZrvZ"
    genius_object = lg.Genius(genius_access_token)

    def __init__(self, lyrics: str) -> None:
        self.lyrics = lyrics

    def search(self) -> None:
        """
        Description: This function prints out the top 10 songs 
        based on the Lyrics entered in by the user.
        Parameters: None
        Return: None
        """
        # top results in dictionary form prouduced from lyrics entered by the user
        results_dict = self.genius_object.search_lyrics(self.lyrics)

        # Grab top results list results from results dictionary
        top_results_list = results_dict['sections'][0]['hits']

        print('\n================================\nTop Results\n================================')
        for i in range(len(top_results_list)):
            lyrics = top_results_list[i]['highlights'][0]['value']
            song = top_results_list[i]['result']['full_title']
            print(f'\nSONG: {song}\nLYRICS: "{lyrics}..."\n')

    def getLyrics(self, song_title: str, artist_name: str) -> None:
        """
        Description: This function prints out the Lyrics based on 
        the Song Title and Artist entered in by the user.
        Parameters: 
        1. title(type:str)-> title of the song.
        2. artist(type:str)-> artist of the song.
        Returns: The Lyrics for the song entered in by the user. 
        """
        # utilize the lyricsgenius search_song method which requires title & artist name
        # and it will search the song we need and returns a dictionary with song info.
        song = self.genius_object.search_song(
            title=song_title, artist=artist_name)
        lyrics = song.lyrics

        # print the lyrics of the song from the song object.
        print("\n"+lyrics)

    # override

    def __str__(self):
        return f"This is the Lyrics Search Box, and the lyrics you entered are: {self.name}"
