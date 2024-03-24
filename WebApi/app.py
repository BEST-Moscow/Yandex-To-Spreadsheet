import logging

from flask import Flask, request

app = Flask(__name__)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


@app.route("/", methods=["POST"])
def parse():
    if request.method == "POST":
        data = request.get_json()
    return ""


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
