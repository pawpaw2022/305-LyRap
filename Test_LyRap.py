"""
Description: This file is to test all the classes required to run
our LyRap Application.

Authors: Grace Gresli, Aidan Pearce, Paul Sining Lu, Bruce Tukuafu
Last Update: 04/26/22

Functions:
1. Demo_LyRap()
2. testLyricsSearchBox()
3. testArtistsSearchBox()
4. testTitleSearchBox()
5. testAddSong()
"""
# from searchBox import SearchBox
from LyricsSearchBox import LyricsSearchBox
from ArtistSearchBox import ArtistSearchBox
from TitleSearchBox import TitleSearchBox
from AddSong import AddSong

class Test_LyRap(object):
    def __init__(self):
        pass

    def Demo_LyRap():
        yes_val = 'y'
        print('\n================================\nWelcome to LyRap\n================================')
        while yes_val == 'y' or yes_val == 'yes' or yes_val == 'Yes':
            # prompts user for input.
            print("\nPlease choose from the following options:")
            print("1. Search by Lyric")
            print("2. Search by Artist Name")
            print("3. Search by Song Title")
            print("4. Add a Song")
            choice = input("\nEnter a value between (1-4): ")

            # makes sure valid user input.
            while choice not in ['1', '2', '3', '4']:
                choice = input(
                    "Invalid choice, please enter a value between (1-4): ")

            # runs the desired feature based on users choice.
            if choice == '1':
                Test_LyRap.testLyricsSearchBox()
            if choice == '2':
                Test_LyRap.testArtistSearchBox()
            if choice == '3':
                Test_LyRap.testTitleSearchBox()
            if choice == '4':
                Test_LyRap.testAddSong()

            # re-runs the program based on user input.
            yes_val = input(
                "\nWould you like to search for another song?(y/n): ")

        print('\nThank you for using LyRap! We hope you come back to search for a lyric or song soon!')

    def testLyricsSearchBox():
        """Runs the tests for our class LyricSearchBox. """
        print('\n================================\nLyric Search Box\n================================')
        print("Please choose from the following options of Lyric Search Box:")
        print("1. Search by Lyric")
        print("2. Get the Lyrics for a song")
        choice = input("\nEnter a value between (1-2): ")

        # checks that input is valid
        while choice not in ['1', '2']:
            choice = input(
                "Invalid choice, please enter a value between (1-2): ")

        if choice == '1':
            phrase = input("Please enter the Lyric:\n")
            lyrics = LyricsSearchBox(phrase)
            lyrics.search()

        if choice == '2':
            song_title = input("Please enter the song title: ")
            artist_name = input("Please enter the artist name: ")

            print('\n')
            lyrics2 = LyricsSearchBox("")
            lyrics2.getLyrics(song_title, artist_name)

    def testArtistSearchBox():
        """Runs the tests for our class ArtistSearchBox"""
        print('\n================================\nArtist Search Box\n================================')

        name = input("Please enter the Artist:\n")
        artist = ArtistSearchBox(name)
        artist.search()

        print('\n')
        resp = input(
            "Do you want to learn more about this artist ? Enter 'y' or 'Y' to confirm: ")
        if resp.lower() == 'y':
            artist.getArtist()

    def testTitleSearchBox():
        """Runs the tests for our class TitleSearchBox"""
        print('\n================================\nTitle Search Box\n================================')

        songname = input("Please enter the title of a song:\n")
        song = TitleSearchBox(songname)
        song.search()
        song.getTitle()
        info = input("Would you also like to see the lyrics to this song? If yes, enter 'y' or 'Y'. If no, enter 'n' or 'N': ")
        if info.lower() == 'y':
            song.showLyrics()
        

    def testAddSong():
        """Runs the tests for our class AddSong"""
        print('\n================================\nAdd Song\n================================')

        title = input("Please enter the Song's Title: ")
        artist = input("Please enter the Song's Artist: ")
        lyrics = input("Enter enter the Song's Lyrics: ")
        
        song = AddSong(title, artist, lyrics)
        song.addSong()


if __name__ == '__main__':
    Test_LyRap.Demo_LyRap()
