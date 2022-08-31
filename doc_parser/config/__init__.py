import os
import sys
from doc_parser.utils.common import read_yaml
# from project_store_exception_layer.exception import CustomException as ConfigurationException
from doc_parser.exception import DocumentException


class Configuration:
    def __init__(self):
        try:
            config = read_yaml("config.yaml")

            FRONTEND_DIR = config['FRONTEND_DIR']
            # KEY_TOKEN = config['KEY_TOKEN']
            DATABASE = config['DATABASE']

            self.TEMPLATE_DIR = FRONTEND_DIR['TEMPLATE_DIR']
            self.STATIC_DIR = FRONTEND_DIR['STATIC_DIR']

            # self.SECRET_KEY = KEY_TOKEN['SECRET_KEY']
            # self.ALGORITHM = KEY_TOKEN['ALGORITHM']

            self.DB_NAME = DATABASE['DB_NAME']
            self.USER = DATABASE['USER']
            self.HOST = DATABASE['HOST']
            self.PORT = DATABASE['PORT']
            self.PASSWORD = DATABASE['PASSWORD']
            self.DATABASE = DATABASE['DATABASE']
        except Exception as e:
            raise DocumentException(e, sys) from e
