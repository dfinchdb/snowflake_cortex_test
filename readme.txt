You can sign up for a Snowflake free trial here:
    https://signup.snowflake.com/

The entire process took less than 2 minutes to have a functional environment in which I could run code both from my IDE and from the UI

The results, however, were extremely slow

Your credentials are entered in the snowflake_config.json file to enable local access. The expected format is:
    {
        "user": "foo",
        "password": "bar",
        "account": "abcdefg-abc12345",
        "warehouse": "COMPUTE_WH",
        "database": "test_database",
        "schema": "test_schema"
    }

Steps to run:
1. Signup for a free trial of Snowflake at https://signup.snowflake.com/
2. Create a database & schema
3. Enter details into snowflake_config.json
    3a. You will need username, password, account, warehouse name, database name, and schema name
    3b. Account can be found by: 
        1. Selecting the bottom icon in the left panel 'Admin'
        2. Selecting 'Account'
        3. In the resulting page, move your cursor over the cell directly under the 'Account' column
        4. When the 'info' icon appears, move your cursor over the icon & copy the url
        5. The account information required is between 'https://' & '.snowflakecomputing.com'
    3c. Warehouse can be found by:
        1. Selecting the bottom icon in the left panel 'Admin'
        2. Selecting 'Warehouse'
        3. In the resulting page, you will find the name of a pre-created warehouse under the 'Name' column