import logging
import json
from api_append import authenticate, export_data_to_sheets
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

        # Authenticate to the service and update the sheet
        service = authenticate()
        if service:  # Only attempt to update the sheet if authentication was successful
            export_data_to_sheets(service, json_data)
        return ""
    abort(500)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
