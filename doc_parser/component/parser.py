import sys
import os
import io
import logging
import numpy as np
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
    def __init__(self, image_file, language):
        try:
            self.image_path = image_file
            self.language = language
            # language will be a hyperparameter
            self.ocr = PaddleOCR(use_angle_cls=True, lang=self.language)
            self.config = Configuration()
        except Exception as e:
            raise DocumentException(e, sys) from e
    def getOcrPrediction(self):
        """getOcrPrediction: This function will return the OCR prediction of the image

        Raises:
            DocumentException: Will raise DocumentException if any error occurs 

        Returns:
            _type_: JSON
        """
        try:
            user_input_path = os.path.join(self.config.artifacts_dir, self.config.input_path, self.config.input_file)
            result_path = os.path.join(self.config.artifacts_dir, self.config.prediction_path, self.config.prediction_file)
            font_file_path = os.path.join(self.config.artifacts_dir, self.config.font_file)
            
            #open byte image
            input_image_file = Image.open(io.BytesIO(self.image_path)).convert('RGB')
            # read image array
            input_image_array = np.array(input_image_file)
            # save image
            input_image_file.save(os.path.join(ROOT, user_input_path))

            # get ocr prediction
            result = self.ocr.ocr(input_image_array, cls=True)

            # image = Image.open(self.image_path).convert('RGB')
            boxes = [line[0] for line in result]
            txts = [line[1][0] for line in result]
            scores = [line[1][1] for line in result]
            im_show = draw_ocr(input_image_file, boxes, txts, scores, font_path=os.path.join(ROOT, font_file_path))
            im_show = Image.fromarray(im_show)

            # save the prediction image
            im_show.save(os.path.join(ROOT, result_path))
            
            # encode the image into base64
            encoded_image = encodeImageIntoBase64(os.path.join(ROOT, result_path)).decode('utf-8')


            return encoded_image, result
        except Exception as e:
            raise DocumentException(e, sys) from e

