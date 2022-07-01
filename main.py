from flask import Flask, render_template
from blueprint_posts.views import blueprint_posts

app = Flask(__name__)
app.register_blueprint(blueprint_posts)

#@app.route('/')
#def index():
 #   return "It works"


if __name__ == '__main__':
    app.run()