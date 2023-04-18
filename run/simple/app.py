import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    message = os.environ.get("MESSAGE", "msg")
    return {"message": "votre message est {}!".format(message)}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))