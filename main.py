import re
import pandas as pd

pattern = r"""
(?P<title>[ \w]*)
\ \(
(?P<author>[\w ]*)
\)\n
# .* on page (\d*) | 
-.*\d*\n
\n
(.*)
"""


def extract(filename, extractedPattern):
    df = pd.DataFrame(columns=["book", "author", "quote"])
    content = open(filename, "r").read()
    for item in re.finditer(extractedPattern, content, re.VERBOSE):
        quote = pd.DataFrame(
            {
                "book": str(item.group(1)),
                "author": str(item.group(2)),
                "quote": str(item.group(3)),
            },
            index=[len(df)],
        )
        df = pd.concat([df, quote])
    return df


print(extract("My Clippings.txt", pattern))
