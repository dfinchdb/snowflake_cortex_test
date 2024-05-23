import snowflake.snowpark as snowpark

from snowflake.snowpark.functions import col
from snowflake.snowpark import Session
import json

with open('snowflake_config.json') as config_file:
    config = json.load(config_file)

new_session = Session.builder.configs(config).create()

cur = new_session.connection.cursor()

cur.execute("SELECT CURRENT_VERSION()").fetchone()
