from distutils.log import debug
from doc_parser.component.parser import DocParser

from typing import Optional
from flask import Flask, request
app = Flask(__name__)


# Take input as image path and give json response
@app.route('/via_postman', methods=["GET", 'POST'])
def image_response():
    if request.method == "POST":
        # get input as image path
        image_path = request.json["image_path"]
        language = request.json["language"]
        doc_parser = DocParser(str(image_path), language)
        encoded_image, result = doc_parser.getOcrPrediction()
        response =  {"result": result, "image": encoded_image}
        return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port = 5000, debug=True)