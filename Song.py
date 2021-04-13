class Song:

    def __init__(self, title):
        self.__title = title
        self.__next_song = None

    # Getter method for the title attribute.
    def get_title(self):
        return self.__title

    # Setter method for the next_song attribute. Make sure titles are type cased to strings and are Title Cased.

    def set_title(self, title):
        self.__title = str(title).capitalize()

    # TODO: Create a getter method for the next_song attribute, called get_next_song

    def get_next_song(self):
        return self.__next_song

    # TODO: Create a setter method for the next_song attribute, called set_next_song

    def set_next_song(self, next_title):
        self.__next_song = next_song

    # TODO: Using the __str___ dunder method, return a string of the song title.

    def __str__(self):
        return (f'{self.__title}')

    # TODO: Using the __repr__ dunder method, return a string formatted as the following:'Song Title -> Next Song Title'

    def __repr__(self):
        return (f'{self.__title} -> {self.__next_song}')
