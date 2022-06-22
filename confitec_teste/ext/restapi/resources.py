from flask import abort, jsonify, request
from flask_restful import Resource
from flask_caching import Cache

from confitec_teste.models import Artist
from flask import current_app

cache = Cache()


class ArtistMusicRankResource(Resource):
    @cache.cached(timeout=604800, query_string=True)
    def get(self, artist_name):
        artist = Artist(artist_name)
        top_10_musics = artist.top_10_musics() or abort(204)

        return jsonify({"artist": artist_name, "musics": top_10_musics})
