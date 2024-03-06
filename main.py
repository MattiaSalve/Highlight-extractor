import re
import os
import pandas as pd

highlights_pattern = r"""
(?P<title>[ \w]*)
\ \(
(?P<author>[\w ]*)
\)\n
# .* on page (\d*) | 
-.*\d*\n
\n
(.*)
"""


def extract(filename, extracted_pattern):
    df = pd.DataFrame(columns=["book", "author", "quote"])
    content = open(filename, "r").read()
    for item in re.finditer(extracted_pattern, content, re.VERBOSE):
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


def write_to_existing_file(file, new_quote):
    f = open(file, "r")
    text = f.read()
    text = text + "\n \n " + new_quote
    f.close()
    f = open(file, "w")
    f.write(text)
    f.close


def write_to_new_file(folder, new_quote):
    f = open(folder + "/" + new_quote["book"] + ".md", "w")
    text = (
        "#BookQuotes\n\n# "
        + new_quote["book"]
        + "\n\n### ~ "
        + new_quote["author"]
        + "\n \n "
        + new_quote["quote"]
    )
    f.write(text)


path = "/Users/mattiasalvetti/Library/Mobile Documents/iCloud~md~obsidian/Documents/MyVault/Book quotes"
quotes = extract("My Clippings.txt", highlights_pattern)
readBooks = os.listdir(path)

for index, row in quotes.iterrows():
    if row["book"] + ".md" not in readBooks:
        write_to_new_file(path, row)
        readBooks = os.listdir(path)
    else:
        file_path = path + "/" + row["book"] + ".md"
        write_to_existing_file(file_path, row["quote"])
