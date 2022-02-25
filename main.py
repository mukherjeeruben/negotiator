from flask import Flask
from flask import render_template
from flask_cors import CORS


flask_app = Flask(__name__)
CORS(flask_app)


@flask_app.route('/')
def aibot():
    return render_template("ai_bot.html")


if __name__ == "__main__":
    flask_app.run(debug=False)