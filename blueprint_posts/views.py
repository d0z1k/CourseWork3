import logging

from flask import Flask, Blueprint, render_template, current_app, abort, request

from blueprint_posts.dao.comment import Comment
from blueprint_posts.dao.comment_dao import CommentDAO
from blueprint_posts.dao.post import Post
from config import DATA_PATH_POSTS, DATA_PATH_COMMENTS
from blueprint_posts.dao.post_dao import PostDAO

# блупринт
blueprint_posts = Blueprint("blueprint_posts", __name__, template_folder="templates")

# Доступ к данным из конфига
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
def page_posts_single(pk: int):
    """
    Определённый пост
    :param pk:
    """
    post: Post | None = post_dao.get_by_pk(pk)
    comments: list[Comment] = comments_dao.get_comments_by_post_id(pk)

    if post is None:
        abort(404)

    return render_template("post_post.html", post=post, comments=comments, comments_len=len(comments))


@blueprint_posts.route("/users/<user_name>")
def page_posts_by_user(user_name: str):
    """
    Возвращает посты по user_name
    :param user_name:
    """

    posts: list[Post] = post_dao.get_by_poster(user_name)

    if not posts:
        abort(404, "user not found")

    return render_template("post_user-feed.html", posts=posts, user_name=user_name)


@blueprint_posts.route("/search/")
def page_posts_search():
    """
    Возвращает посты по user_name
    """
    s: str = request.args.get("s", "")

    if s == "":
        posts: list = []
    else:
        posts = post_dao.search_in_content(s)

    return render_template("post_search.html", posts=posts, s=s, posts_len=len(posts))
