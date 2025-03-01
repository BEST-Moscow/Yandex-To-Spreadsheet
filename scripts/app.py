import logging
import json
import os
from .googleApi import append
from flask import Flask, request, abort, Response

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
        numOfList = json_data["table"]
        
        logging.info("Data fetched")

        # ID of the line, where the data will be placed
        # Save to file to save last id of the line after shutdown
        with open(f"{os.getcwd()}/id.txt", "r") as file:
            id1 = int(file.read())
            
        with open(f"{os.getcwd()}/id_2.txt", "r") as file:
            id2 = int(file.read())
        
        with open(f"{os.getcwd()}/id_3.txt", "r") as file:
            id3 = int(file.read())
        
        id = [id1, id2, id3]    
        
        # Caching data in the data.json file
        with open(f"{os.getcwd()}/data.json", 'a') as file:
            file.write(data + ",\n")

        # Authenticate to the service and update the sheet
        service = append.authenticate()
        if service:  # Only attempt to update the sheet if authentication was successful
            append.export_data_to_sheets(service, json_data, id, numOfList)
            
    return Response("", status=201)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
