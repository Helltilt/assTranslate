#!/usr/bin/env python3
from textblob import TextBlob
import itertools
import argparse
import sys
import re

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i",
                        "--input",
                        dest="input",
                        action="store",
                        default=None,
                        required=True,
                        help="input ass filename")
arg_parser.add_argument("-l",
                        "--lang",
                        dest="lang",
                        action="store",
                        default=None,
                        required=True,
                        help="destination language")
args = arg_parser.parse_args()

dialogue_regex = re.compile(r"(?:Dialogue.*\d+,\d+,\d+,"
                            r"(?:\w*\s*)*,)(?:{.*})*(.+)")
comment_regex = re.compile(r"{.*}")
newline_regex = re.compile(r"(\w)?\\N(\w)?")

spinner = itertools.cycle(["-", "/", "|", "\\"])
out_name = args.lang + "_" + args.input
with open(args.input, "r", encoding="utf-8") as ass:
    out_file = open(out_name, "w", encoding="utf-8")
    print("Starting translating...")
    for line in ass:
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        sys.stdout.write('\b')
        if not dialogue_regex.match(line):
            # writes unchanged lines in the ass
            out_file.write(line)
        for dialogue in dialogue_regex.findall(line):
            # exclude inline comments/tags from translation
            stripped_dialogue = re.sub(comment_regex, "", dialogue)
            # remove newlines
            stripped_dialogue = re.sub(newline_regex, r"\1 \2", stripped_dialogue)
            blob = TextBlob(stripped_dialogue.strip())
            try:
                blob = blob.translate(to=args.lang)
            except:
                print("Couldn't translate line: " + str(blob))
                pass
            translated = line.replace(dialogue, str(blob))
            out_file.write(translated)
print("Translated file saved as " + out_name)
out_file.close()
