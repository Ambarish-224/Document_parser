import os
import sys
from doc_parser.utils.common import read_yaml
# from project_store_exception_layer.exception import CustomException as ConfigurationException
from doc_parser.exception import DocumentException


class Configuration:
    def __init__(self):
        try:
            config = read_yaml(os.path.join(os.getcwd(), "configs", "config.yaml"))

            artifacts = config['artifacts']
            # KEY_TOKEN = config['KEY_TOKEN']

            self.artifacts_dir = artifacts['artifacts_dir']
            self.input_path = artifacts['input_path']
            self.prediction_path = artifacts['prediction_path']
            self.font_file = artifacts['font_file']
            self.prediction_file = artifacts['prediction_file']
            self.input_file = artifacts['input_file']
        except Exception as e:
            raise DocumentException(e, sys) from e
