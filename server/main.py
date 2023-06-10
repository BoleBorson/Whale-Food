from typing import Union
import pytesseract
from PIL import Image
from fastapi import FastAPI, UploadFile, File, Form, Request
import json
from fastapi.responses import JSONResponse
from chat import format_receipt
from pocketbase import PocketBase  # Client also works the same
from pocketbase.client import FileUpload
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from dotenv import load_dotenv
import os

load_dotenv()

client = PocketBase('http://{0}:8090'.format(os.environ.get('POCKET')))

# authenticate as regular user
user_data = client.collection("users").auth_with_password("joe", "joejoejoe")

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    # Add any other allowed origins here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/extract_text")
async def extract_text(file: UploadFile = File(...), charge: str = Form(...), token: str = Form(...)):
    image = Image.open(file.file)

    text = pytesseract.image_to_string(image)

    formatted_receipt = format_receipt(text)
    
    client.collection("receipts").create(
    {
        "data": formatted_receipt,
        "user": token,
        "charge": charge,
        "rec": FileUpload((file.filename, file.file))
    })

    return JSONResponse(content={"status": "success"})

@app.get("/rec-stats")
async def rec_stats():
    recs = client.collection("receipts").get_list()
    
    print(recs.items)

            

    return JSONResponse(content={"status": "success"})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)