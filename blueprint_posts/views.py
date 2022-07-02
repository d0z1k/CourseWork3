from flask import Flask, Blueprint, render_template, current_app, abort

from blueprint_posts.dao.comment import Comment
from blueprint_posts.dao.comment_dao import CommentDAO
from config import DATA_PATH_POSTS, DATA_PATH_COMMENTS
from blueprint_posts.dao.post_dao import PostDAO

# блупринт
blueprint_posts = Blueprint("blueprint_posts", __name__, template_folder="templates")

#Доступ к данным из конфига
post_dao = PostDAO(DATA_PATH_POSTS)
comments_dao = CommentDAO(DATA_PATH_COMMENTS)


@blueprint_posts.route("/")
def page_posts_index():
    """
    Все посты
    """
    all_posts = post_dao.get_all()
    return render_template("post_index.html", posts=all_posts)


@blueprint_posts.route("/posts/<int:pk>/")
def page_posts_single(pk):
    """
    Определённый пост
    :param pk:
    """
    post = post_dao.get_by_pk(pk)
    comments: list[Comment] = comments_dao.get_comments_by_post_id(id)

    if post is None:
        abort(404)

    return render_template("post_post.html", post=post)
