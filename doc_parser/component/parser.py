import sys
import os
import logging
from PIL import Image
from doc_parser.utils.common import read_yaml, create_directories, decodeImage, encodeImageIntoBase64
from paddleocr import PaddleOCR,draw_ocr
from doc_parser.config import Configuration
from doc_parser.exception import DocumentException

ROOT = os.getcwd()
STAGE = "Doc Parser" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )
class DocParser:
    def __init__(self, image_path, language):
        try:
            self.image_path = image_path
            self.language = language
            # language will be a hyperparameter
            self.ocr = PaddleOCR(use_angle_cls=True, lang=self.language)
            self.config = Configuration()
        except Exception as e:
            raise DocumentException(e, sys) from e
    def getOcrPrediction(self):
        try:
            result_path = os.path.join(self.config.artifacts_dir, self.config.prediction_path, self.config.prediction_file)
            font_file_path = os.path.join(self.config.artifacts_dir, self.config.font_file)

            result = self.ocr.ocr(self.image_path, cls=True)

            image = Image.open(self.image_path).convert('RGB')
            boxes = [line[0] for line in result]
            txts = [line[1][0] for line in result]
            scores = [line[1][1] for line in result]
            im_show = draw_ocr(image, boxes, txts, scores, font_path=os.path.join(ROOT, font_file_path))
            im_show = Image.fromarray(im_show)
            im_show.save(os.path.join(ROOT, result_path))
            encoded_image = encodeImageIntoBase64(os.path.join(ROOT, result_path)).decode('utf-8')


            return encoded_image, result
        except Exception as e:
            raise DocumentException(e, sys) from e

