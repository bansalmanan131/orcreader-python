import pymongo
from pymongo import MongoClient
from PIL import Image
import pytesseract

cluster = MongoClient("mongodb+srv://bansalmanan131:BANSALMANAN!#!@cluster0.fdg3i.gcp.mongodb.net/ocr?retryWrites=true&w=majority")
db=cluster["ocr"]
collection=db["ocrreader"]
im=Image.open("test.jpeg")
text=pytesseract.image_to_string(im, lang="eng")
post={"_id":1, "name":"test", "text in file":text}

collection.insert_one(post)

