"""
This file is to test all the classes. 
"""
from SearchBox import SearchBox
from LyricsSearchBox import LyricsSearchBox
from ArtistSearchBox import *
from TitleSearchBox import *

class Test_LyRap(object):
    def __init__(self):
        pass
    def main():
        yes_val = 'y'
        print('\n================================\nWelcome to LyRap\n================================')
        while yes_val == 'y':
            # prompts user for input.
            print("Please choose from the following options:") 
            print("1. Search by Lyric")
            print("2. Search by Artist Name")
            print("3. Search by Song Title") 
            print("4. Add a Song")
            choice = input("\nEnter a value between (1-4): ")
            # makes sure valid user input.
            while choice not in ['1', '2', '3', '4']:
                choice = input("Invalid choice, please enter a value between (1-4): ")

            if choice == '1':
                phrase = input("Please enter the Lyric:\n")
                lyrics = LyricsSearchBox(phrase)
                lyrics.searchByLyrics()
            if choice == '2':
                pass
            if choice == '3':
                pass
            if choice == '4':
                pass
            yes_val = input("Would you like to search for another song? (y/n)")
        print('\nThank you for using LyRap! We hope you come back to search for a lyric or song soon!')


                

if __name__ == '__main__':
    Test_LyRap.main()