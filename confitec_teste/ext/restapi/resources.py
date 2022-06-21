from flask import abort, jsonify
from flask_restful import Resource

from confitec_teste.models import Artist


class ArtistMusicRankResource(Resource):
    def get(self, artist_name):
        artist = Artist(artist_name)
        top_10_musics = artist.top_10_musics() or abort(204)

        return jsonify({"artist": artist_name, "musics": top_10_musics})
