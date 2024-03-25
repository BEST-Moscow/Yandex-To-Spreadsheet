import logging
import json
from flask import Flask, request, abort

app = Flask(__name__)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


@app.route("/", methods=["POST"])
def parse():
    if request.method == "POST":
        json_data = request.get_json()
        data = json.dumps(json_data, ensure_ascii=False)

        logging.info("Data fetched")
        with open("test.json", 'w') as file:
            file.write(data)
        return ""
    abort(500)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

