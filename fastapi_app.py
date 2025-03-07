from fastapi import FastAPI
from sythesizer import synthesizer

app = FastAPI()

def synthesize_json_data():
    data_types = {
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
        "unsupported_field": "unknown_type"
    }

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/generate_data")
async def generate_data():
    return test_synthesize_json_data()

@app.get("/generate_multiple/{count}")
async def generate_multiple(count: int):
    return [test_synthesize_json_data() for _ in range(count)]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
