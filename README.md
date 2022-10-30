![alt text](https://github.com/Rishav-hub/face_auth_dev/blob/b440f8d95722e3c26a917011a3f89c7aed7b711a/docs/68747470733a2f2f696e6575726f6e2e61692f696d616765732f696e6575726f6e2d6c6f676f2e706e67.png?raw=true)

# 📙 Document scanner
Document Scanner has a huge application in domains like aviation, Banking etc. It helps to extract important information from the documents, which reduces manual work to a huge extent. Here we have built an API which will have an input of a image and the language which it should extract. It will give response of text that is exracted and Image with the area of response. We have used PaddleOCR, which is a Package for text extraction, which is a Python library. This application has been manually deployed using AWS services, AWS App runner and AWS ECR.

## 💿 Installing

#### 1. Environment setup.
```commandline
conda create --prefix ./env python=3.8 -y
conda activate ./env
```

#### 2. Install Requirements
```commandline
pip install -r requirements.txt
```

#### 3. Run the setup
```commandline
pip install -e .
```

#### 5. Run Application
windows
```commandline
python app.py 
```

## 🚀 API testing using FastAPI Swagger UI

URI to be used -: ```http://localhost:5000/docs```

<img width="748" alt="image" src="https://user-images.githubusercontent.com/57321948/198568854-d3eb0073-3652-46e1-aac2-c2dbea97ba43.png">



<img width="791" alt="image" src="https://user-images.githubusercontent.com/57321948/198568983-24ecc11f-3937-430d-90b6-ada4c3c370e7.png">

## Deployment to AWS App Service.
For Deployment please refer [this](https://github.com/ketangangal/Document_parser/blob/main/docs/manual_deploy.MD).

## 🔧 Built With
- FastAPI
- Python 3.8
- Postman
- AWS App Runner
- AWS ECR

## 🏦 Industrial Use cases 
- Document archiving
- Invoice processing
- Passport & ID Card recognition
- Automated contract preparation
- Automated document processing

## ✌️ Conclusion
We have shown how to build and Deploy your own document parsere in simple steps using paddleocr.


