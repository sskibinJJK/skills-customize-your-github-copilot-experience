# Starter code for FastAPI REST API assignment

# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI REST API!"}

# Add CRUD endpoints for 'items' in this file as you complete the assignment.
