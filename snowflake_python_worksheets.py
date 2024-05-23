# The Snowpark package is required for Python Worksheets.
# You can add more packages by selecting them using the Packages control and then importing them.

import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col
from snowflake.cortex import Complete, ExtractAnswer, Sentiment, Summarize, Translate


def main(session: snowpark.Session) -> str:
    text = """
        The Snowflake company was co-founded by Thierry Cruanes, Marcin Zukowski,
        and Benoit Dageville in 2012 and is headquartered in Bozeman, Montana.
    """
    output = f"""
    Complete = '{Complete("llama2-70b-chat", "how do snowflakes get their unique patterns?")}
    ExtractAnswer = '{ExtractAnswer(text, "When was snowflake founded?")}'
    Sentiment = '{Sentiment("I really enjoyed this restaurant. Fantastic service!")}'
    Summarize = '{Summarize(text)}'
    Translate = '{Translate(text, "en", "fr")}'"""
    return output
