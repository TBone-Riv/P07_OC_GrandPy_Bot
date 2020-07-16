import re
from config import PARSE_REGEX


class Question:
    def __init__(self, user_input:str):
        self.user_input = user_input

    def parse(self):
        for regex in PARSE_REGEX:
            parse = re.search(regex, self.user_input)

            if parse:
                parse = parse.group(2)
                return parse

