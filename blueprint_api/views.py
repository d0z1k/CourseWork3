from flask import Blueprint, jsonify

blueprint_api = Blueprint("blueprint_api", __name__)


@blueprint_api.route("/posts/")
def api_posts_all():
    return jsonify({"data": "all posts"})


@blueprint_api.route("/posts/<int:pk>/")
def api_post_by_pk(pk: int):
    return jsonify({"data": "single post"})
