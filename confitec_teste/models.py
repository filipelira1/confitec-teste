from lyricsgenius import Genius
import uuid
import boto3


class Artist:
    def __init__(self, artist_name: str) -> None:
        self.artist_name = artist_name

    def top_10_musics(self) -> list:
        genius = Genius()
        genius.verbose = False
        artist = genius.search_artist(self.artist_name, max_songs=10, sort="popularity")
        songs = [song.title for song in artist.songs] if artist else []
        if songs:
            transacao = uuid.uuid4()
            dynamodb = boto3.client("dynamodb")
            dynamodb.put_item(
                TableName="artists.musics",
                Item={
                    "transacao": transacao,
                    "artist": self.artist_name,
                    "musics": songs,
                },
            )

        return songs
