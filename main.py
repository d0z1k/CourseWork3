from flask import Flask, render_template
from blueprint_posts.views import blueprint_posts


def create_and_config_app(config_path):

    app = Flask(__name__)
    app.register_blueprint(blueprint_posts)
    app.config.from_pyfile(config_path)
    return app


app = create_and_config_app("config.py")

if __name__ == '__main__':
    app.run()
