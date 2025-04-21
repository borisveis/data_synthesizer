import io.restassured.RestAssured;
import io.restassured.response.Response;
import org.testng.Assert;
import org.testng.annotations.Test;

public class RestAssuredTests {

    private final String baseUri = "http://0.0.0.0:8000";

    @Test
    public void generator_contains_full_name() {
        Response response = RestAssured
                .given()
                .baseUri(baseUri)
                .when()
                .get()
                .then()
                .statusCode(200)
                .extract()
                .response();

        String body = response.getBody().asString();
        Assert.assertTrue(body.contains("full_name"), "Homepage should contain the word 'full_name'");
    }

    // @Test
    // public void googleHomePageShouldContainGoogleInTitle_with_chained() {
    //     Response response = RestAssured
    //             .given()
    //             .baseUri("https://www.google.com")
    //             .header("Accept", "text/html")
    //             .log().all()
    //             .when()
    //             .get("/")
    //             .then()
    //             .statusCode(200)
    //             .extract()
    //             .response();

    //     String body = response.getBody().asString();
    //     Assert.assertTrue(body.contains("Google"), "Google homepage should contain the word 'Google'");
    // }
}
