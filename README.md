# data_synthesizer
arbitrary json data synthesizer for model validation
ADded basic Java Restassured tests that can be executed after the api app is started.
***executing Restassured tests***
1. Install Maven dependencies 'cd java-tests'; maven 'clean install'
2. Start FastAPI app. Run 'rest_api_app/fastapi_app.py'
3. Execute tests in java-tests/src/test/java/RestAssuredTests.java