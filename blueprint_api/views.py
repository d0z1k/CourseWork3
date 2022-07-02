import logging

from flask import Blueprint, jsonify

from blueprint_posts.dao.comment_dao import CommentDAO
from blueprint_posts.dao.post import Post
from config import DATA_PATH_POSTS, DATA_PATH_COMMENTS
from blueprint_posts.dao.post_dao import PostDAO

# блупринт
blueprint_api = Blueprint("blueprint_api", __name__)

# Доступ к данным из конфига
post_dao = PostDAO(DATA_PATH_POSTS)
comments_dao = CommentDAO(DATA_PATH_COMMENTS)

api_logger = logging.getLogger("api_logger")


@blueprint_api.route("/posts/")
def api_posts_all():
    """
    Все посты(endpoints)
    """
    all_posts = post_dao.get_all()
    api_logger.debug("Запрошены все посты")
    return jsonify([post.as_dict() for post in all_posts]), 200


@blueprint_api.route("/posts/<int:pk>/")
def api_post_by_pk(pk: int):
    """
    Определённый пост (endpoints)
    :param pk:
    """

    post: Post | None = post_dao.get_by_pk(pk)

    return jsonify(post.as_dict()), 200

