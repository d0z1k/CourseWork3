from flask import Flask, Blueprint, render_template, current_app, abort
from config import DATA_PATH_POSTS
from blueprint_posts.dao.post_dao import PostDAO

blueprint_posts = Blueprint("blueprint_posts", __name__, template_folder="templates")
post_dao = PostDAO(DATA_PATH_POSTS)


@blueprint_posts.route("/")
def page_posts_index():
    all_posts = post_dao.get_all()
    return render_template("post_index.html", posts=all_posts)


@blueprint_posts.route("/posts/<int:pk>/")
def page_posts_single(pk):
    post = post_dao.get_by_pk(pk)

    if post is None:
        abort(404)

    return render_template("post_post.html", post=post)
