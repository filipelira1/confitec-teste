from lyricsgenius import Genius


class Artist:
    def __init__(self, artist_name: str) -> None:
        self.artist_name = artist_name

    def top_10_musics(self) -> list:
        genius = Genius()
        genius.verbose = False
        artist = genius.search_artist(self.artist_name, max_songs=10, sort="popularity")

        return [song.title for song in artist.songs] if artist else []
