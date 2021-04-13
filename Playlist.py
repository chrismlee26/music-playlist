from Song import Song


class Playlist:
    def __init__(self):
        self.__first_song = None

    # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.
    def add_song(self, title):
        # new_song = Song(title)
        # append new_song to playlist

        # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index.
        # The method has one parameter, title, which is the title of the song to be searched for. If the song is found, return its index. Otherwise, return -1.

    def find_song(self, title):
        pass
        # create loop_var = 0 (looking for index)
        # for loop over songs list
        # if title = False
        # return -1,
        # else if title = True,
        # return loop_var

    # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed.

    def remove_song(self, title):
        pass
        # create title_var from input()
        # for loop over songs list
        # if title = True
        # remove Title
        # else if title = False,
        # return "song not found"

    # TODO: Create a method called length, which returns the number of songs in the playlist.

    def length(self):
        pass
        # song_count = len(playlist)
        # return song_count

    # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

    # Example:
    # 1. Song Title 1
    # 2. Song Title 2
    # 3. Song Title 3

    def print_songs(self):
        pass
        # song_index = 0
        # for loop over songs list
        #    # if songs_list >= 1
        #    # maybe count at song_index
        #    # return index, and list :S
