from fastapi import FastAPI, HTTPException, Depends , HTTPException, Header
from pydantic import BaseModel
import os
from utils import *
from models import *


app = FastAPI()

# Replace with your API details
LICENSE_API_URL = ""
API_USERNAME = os.getenv("API_USERNAME","")
API_PASSWORD = os.getenv("API_PASSWORD","")

# Dependency for license validation
def validate_request_license(license_key: str):
    result = validate_license(LICENSE_API_URL, license_key)
    if not result.get("valid", False):
        raise HTTPException(status_code=403, detail="Invalid license")
    return result

@app.post("/validate-license")
def validate_license_endpoint(x_license_key: str = Header(...)):
    """
    Validate the license using the X-License-Key header.
    """
    validation_result = validate_license(LICENSE_API_URL, x_license_key,API_USERNAME,API_PASSWORD)
    if not validation_result:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return {"message": "API Key is valid", "details": validation_result}

@app.get("/protected")
def your_endpoint(x_license_key: str = Header(...)):
    """
    Example endpoint with license validation middleware.
    """
    # Validate the license
    validation_result = validate_license(LICENSE_API_URL, x_license_key,API_USERNAME,API_PASSWORD)
    if not validation_result:
        raise HTTPException(status_code=403, detail="Invalid API Key")

    # Proceed with the main logic
    return {"message": "Request processed successfully"}