from fastapi import FastAPI
from data_synthesizer import synthesizer
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class DataTypesRequest(BaseModel):
    data_types: Dict[str, str]

def synthesize_json_data(data_types):
    return data_synthesizer.synthesize_json_data(data_types)

@app.get("/")
async def root():
    default_data_types = {
        "full_name": "name",
        "user_email": "email",
        "contact_number": "phone_number",
        "home_address": "address",
        "random_text": "text",
        "age": "integer",
        "salary": "float",
        "is_active": "boolean",
        "dob": "date",
        "last_login": "datetime",
        # "unsupported_field": "unknown_type"
    }
    output = synthesize_json_data(default_data_types)
    return output

@app.post("/synthesize")
async def synthesize_data(request: DataTypesRequest):
    output = synthesize_json_data(request.data_types)
    return output

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
