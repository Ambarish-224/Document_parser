![alt text](https://github.com/Rishav-hub/face_auth_dev/blob/b440f8d95722e3c26a917011a3f89c7aed7b711a/docs/68747470733a2f2f696e6575726f6e2e61692f696d616765732f696e6575726f6e2d6c6f676f2e706e67.png?raw=true)

# 📙 Document scanner
Document Scanner has a huge application in domains like aviation, Banking etc. It helps to extract important information from the documents, which reduces manual work to a huge extent. Here we have built an API which will have an input of a image and the language which it should extract. It will give response of text that is exracted and Image with the area of response. We have used PaddleOCR, which is a Package for text extraction, which is a Python library.

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

## 🚀 API testing using Postman

URI to be used -: ```http://127.0.0.1:5000/via_postman```

<img width="869" alt="image" src="https://user-images.githubusercontent.com/57321948/187866575-1d158199-3d78-4fc9-9f4e-dd9e0be95859.png">



<img width="1207" alt="image" src="https://user-images.githubusercontent.com/57321948/187869364-229b60d4-5398-47d8-af20-e6c9b0a54d93.png">

## 🔧 Built With
- Flask
- Python 3.8
- Postman

## 🏦 Industrial Use cases 
- Document archiving
- Invoice processing
- Passport & ID Card recognition
- Automated contract preparation
- Automated document processing

## ✌️ Conclusion
We have shown how to build your own document parsere in simple steps using paddleocr.


