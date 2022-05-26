"""
DESCRIPTION: ADDSONG is a subclass of SearchBox and allows
the user to add a song using user entered atrist, song title and song.
The results will produce the a new songLibrary the contains all new user added songs in a seperate txt file.

AUTHORS: Grace Gresli

LAST UPDATE: 5/12 @4:21

Class Variables: 
1. genius_access_token -> str(allows access to genius API)
2. genius_object -> instantiation of genius object which allows access
to methods of the genius API.

Functions:
1. AddSong()
2. getLyrics()
3. getArtist()
4. getYear()
5. __str__()

"""
import lyricsgenius as lg


class AddSong(object):

    genius_access_token = "_rDAy259SoA7baRL1ouy2MWdOADsdevMvTvMxo83XXtJJ-ejmfSNvtZSrbqJZrvZ"
    genius_object = lg.Genius(genius_access_token)

    def __init__(self, title: str, artist: str, lyrics: str) -> None:
        self.title = title
        self.lyrics = lyrics
        self.artist = artist

    def getTitle(self):
        return self.title

    def getLyrics(self):
        return self.lyrics

    def getArtist(self):
        return self.artist

    def addSong(self):

        try:
            filename = "newSongLibrary.txt"
            with open(filename, "w") as f:
                while True:
                    try:
                        f.write("Song Title: " + self.title + "\n" + "Song Artist: " +
                                self.artist + "\n" + "Song Lyrics: " + self.lyrics + "\n")
                        f.write("\n")
                        f.close()  # with and as closes the file autamatically
                    except EOFError:
                        break
        except:
            print("Song Successfuly Added!")

    # override
    def __str__(self):
        return f"This is the Add Song feature, and the Song title you entered is: {self.title}, by: {self.artist}."
