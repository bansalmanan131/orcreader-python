import pymongo
import io
from pymongo import MongoClient
from PIL import Image
import pytesseract
from wand.image import Image as wi

cluster = MongoClient("mongodb+srv://bansalmanan131:BANSALMANAN!#!@cluster0.fdg3i.gcp.mongodb.net/ocr?retryWrites=true&w=majority")
db=cluster["ocr"]
collection=db["ocrreader"]

pdf = wi(filename = "cs1.pdf", resolution = 300)
pdfImg = pdf.convert('jpeg')

imgBlobs = []

for img in pdfImg.sequence:
	page = wi(image = img)
	imgBlobs.append(page.make_blob('jpeg'))

extracted_text = []

for imgBlob in imgBlobs:
	im = Image.open(io.BytesIO(imgBlob))
	text = pytesseract.image_to_string(im, lang = 'eng')
	extracted_text.append(text)

post={"name":"test", "text in file":extracted_text}

collection.insert_one(post)
