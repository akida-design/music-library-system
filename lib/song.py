class Song:
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artists_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # To update tracking

        Song.add_song_to_count()
        Song.add_genres(genre)
        Song.add_artists(artist)
        Song.update_genre_count(genre)
        Song.update_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_genres(cls, genre):
        cls.genres.add(genre)

    @classmethod
    def add_artists(cls, artist):
        cls.artists.add(artist)

    @classmethod
    def update_genre_count(cls, genre):
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1

    @classmethod
    def add_artists_count(cls, artist):
        if artist not in cls.artists_count:
            cls.artists_count[artist] = 1
        else:
            cls.artists_count[artist] += 1
