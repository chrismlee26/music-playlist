from Song import Song


class Playlist:
    def __init__(self):
        # Set root to None
        self.__first_song = None

    # The method 'add_song' creates a Song object and adds it to the playlist.
    # This method has one parameter called title.
    def add_song(self, title):
        # This is the HEAD, use a first song to link to other songs
        # Create a "new_song" using the node from "Song.py".
        new_song = Song(title)
        # Use the "new_song" to call "set_next_song()" linked to "__first_song". This creates the LL's Head.
        new_song.set_next_song(self.__first_song)
        self.__first_song = new_song

    # The method 'find_song' searches for whether a song exits in the playlist and returns its index.
    # The method has one parameter, title, which is the title of the song to be searched for. If found it returns the song's index.
    def find_song(self, title):
        # Traverse LL to find target title.
        i = 0
        current_song = self.__first_song

        while current_song != title:
            if current_song.get_next_song() == None:
                return False

            current_song = current_song.get_next_song()
            i += 1
        return i

    # The method 'remove_song' removes a song from the playlist. This method takes one parameter, title, which is the song to be removed.
    def remove_song(self, title):
        # Remove doesn't explicitly delete. Make address before point to next -- this disconnects from the chain.
        current_song = self.__first_song

        if current_song.get_title() == title:
            self.__first_song = current_song.get_next_song()
            return True

        while current_song.get_next_song().get_title() != title:
            if current_song.get_next_song() == None:
                return False

        current_song = current_song.get_next_song()
        remove_song = current_song.get_next_song()
        print("Song removed")

    # The method 'length' returns the number of songs in the playlist.
    def length(self):
        counter = 0
        current_song = self.__first_song
        while current_song != None:
            counter += 1
            current_song = current_song.get_next_song()
        return counter

    # The method 'print_songs' prints a numbered list of the songs in the playlist.
    def print_songs(self):
        counter = 0
        current_song = self.__first_song

        while current_song != None:
            counter += 1
            print(f"{counter}. {current_song.get_title()}")
            current_song = current_song.get_next_song()

        if counter == 0:
            print("No Songs loaded!")
            return False
