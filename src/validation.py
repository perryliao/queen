import re

def validateMention(msg):
    print(msg)
    return re.search("^<@[0-9]+>", msg)
