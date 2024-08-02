from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

class Details(BaseModel):
    data: List[str]

@app.post("/bfhl")
async def post_details(request: Details):
    print(request.data)
    user_id = "john_doe_17091999"
    email = "john@xyz.com"
    roll_number = "ABCD123"
    numbers = []
    alphabets = []

    for item in request.data:
        if item.isdigit():
            numbers.append(item)
        elif item.isalpha():
            alphabets.append(item)

    highest_alphabet = []
    if alphabets:
        highest_alphabet_char = alphabets[0]
        for char in alphabets:
            if char.lower() > highest_alphabet_char.lower():
                highest_alphabet_char = char
        highest_alphabet = [highest_alphabet_char]

    return JSONResponse(
        content={
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        },
        status_code=200  # Ensure HTTP 200 OK status
    )

@app.get("/bfhl")
async def get_details():
    return JSONResponse(
        content={"operation_code": 1},
        status_code=200  # Ensure HTTP 200 OK status
    )
