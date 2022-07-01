from flask import Flask, Blueprint, render_template

blueprint_posts = Blueprint("blueprint_posts", __name__, template_folder="templates")


@blueprint_posts.route("/")
def page_posts_index():
    return render_template("post_index.html")
