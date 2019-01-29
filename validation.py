import re

def validateMention(msg):
    print(msg)
    return re.search("<@[1-9]+>", msg)
