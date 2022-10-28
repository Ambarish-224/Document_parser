from distutils.log import debug
import uvicorn
from doc_parser.component.parser import DocParser
from doc_parser.exception import DocumentException
from fastapi.responses import JSONResponse

from typing import Optional
from fastapi import APIRouter, File, Request, FastAPI
from fastapi.responses import JSONResponse
app = FastAPI()

@app.post("/via_postman")
async def image_response(image_file: bytes = File(...), language: str = "en"):
    try:
        doc_parser = DocParser(image_file, language)
        encoded_image, result = doc_parser.getOcrPrediction()
        response =  JSONResponse(content={"result": result, "image": encoded_image}, status_code=200)
        return response
    except DocumentException as e:
        raise e

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port = 5000)