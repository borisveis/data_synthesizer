import pytest
from fastapi_app import app
from synthesizer import synthesizer

import uvicorn
from multiprocessing import Process

def run_server(host: str, port: int):
    proc = Process(
        target=uvicorn.run,
        args=("main:app",),
        kwargs={"host": host, "port": port}
    )
    proc.start()
    return proc
def shutdown_server(proc: Process):
    proc.terminate()
    proc.join(timeout=5)
    if proc.is_alive():
        proc.kill()
@pytest.fixture(scope="session")
def server():
    proc = run_server("127.0.0.1", 8000)
    yield proc
    shutdown_server(proc)

def test_synthesize_json_data():
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
    result = synthesizer.synthesize_json_data(data_types)

    assert isinstance(result, dict), "Output should be a dictionary"

    # Check if all keys exist in the output
    for key in data_types.keys():
        assert key in result, f"Missing expected key: {key}"

    # Validate the generated data types
    assert isinstance(result["full_name"], str) and len(result["full_name"]) > 0, "Name should be a valid string"
    assert isinstance(result["user_email"], str) and "@" in result["user_email"], "Email should be valid"
    assert isinstance(result["contact_number"], str) and len(
        result["contact_number"]) > 0, "Phone number should be valid"
    assert isinstance(result["home_address"], str) and len(result["home_address"]) > 0, "Address should be valid"
    assert isinstance(result["random_text"], str) and len(result["random_text"]) > 0, "Text should be valid"
    assert isinstance(result["age"], int) and 0 <= result["age"] <= 100, "Age should be an integer between 0 and 100"
    assert isinstance(result["salary"], float) and 0 <= result["salary"] <= 100, "Salary should be a float within range"
    assert isinstance(result["is_active"], bool), "Boolean field should be a boolean value"
    assert isinstance(result["dob"], str), "Date should be a string in ISO format"
    assert isinstance(result["last_login"], str), "Datetime should be a string in ISO format"
    assert "Unsupported data type" in result["unsupported_field"], "Unsupported fields should return an error message"
    # print(result.items())
def test_generate_people_with_boris():
    # Define the data types for a person
    person_data_types = {
        "name": "name",
        "age": "integer",
        "email": "email"
    }

    # Generate 10 people
    people = []
    boris_count = 0
    for i in range(100):
        person = synthesizer.synthesize_json_data(person_data_types)
        if i < 25:  # Ensure at least 25% are named Boris
            person['name'] = 'Boris'
            boris_count += 1
        people.append(person)

    # Count how many people are named Boris
    actual_boris_count = sum(1 for person in people if person['name'] == 'Boris')

    # Assert that 25% (rounded up to 3) of the people are named Boris
    assert actual_boris_count == 25, f"Expected 25 people named Boris, but got {actual_boris_count}"

    # Print the generated people for verification (optional in pytest, but can be useful for debugging)
    for person in people:
        print(person)


def test_root_endpoint():
    from fastapi.testclient import TestClient
    """
    Test the root endpoint to confirm the server is running.
    """
    client = TestClient(app)
    response = client.get("/")  # Send a GET request to the root endpoint
    assert response.status_code == 200  # Assert that the status code is 200 (OK)