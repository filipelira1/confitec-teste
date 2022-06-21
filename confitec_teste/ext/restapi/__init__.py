from flask import Blueprint
from flask_restful import Api

from .resources import ArtistMusicRankResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(ArtistMusicRankResource, "/<artist_name>/top-10-musics")
    app.register_blueprint(bp)
