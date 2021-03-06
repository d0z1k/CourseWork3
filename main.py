from flask import Flask, render_template

from blueprint_api.views import blueprint_api
from blueprint_posts.views import blueprint_posts
from exceptions.exceptions import DataSourceError

import logger


def create_and_config_app(config_path):
    app = Flask(__name__)
    app.register_blueprint(blueprint_posts)
    app.register_blueprint(blueprint_api, url_prefix='/api')
    app.config.from_pyfile(config_path)
    logger.config(app)
    return app


app = create_and_config_app("config.py")


@app.errorhandler(404)
def page_error_404(error):
    return f"Этой страницы не существует, а могла бы - {error}", 404


@app.errorhandler(500)
def page_error_404(error):
    return f"Дело не в тебе, дело во мне - {error}", 500


@app.errorhandler(DataSourceError)
def page_error_data_source_error(error):
    return f"Наш Джейсон - не Момоа, может и сломаться - {error}", 500


if __name__ == '__main__':
    app.run()
