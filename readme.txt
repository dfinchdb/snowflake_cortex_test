You can sign up for a Snowflake free trial here:
    https://signup.snowflake.com/

The entire process took less than 2 minutes to have a functional environment in which I could run code both from my IDE and from the UI

Your credentials are entered in the snowflake_config.json file to enable local access. The expected format is:
    {
        "user": "user_name",
        "password": "password",
        "account": "izxbdfz-xua73777",
        "warehouse": "COMPUTE_WH",
        "database": "test",
        "schema": "test_schema"
    }