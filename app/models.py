import re
from config import PARSE_REGEX


class Question:
    def __init__(self, user_input:str):
        self.user_input = user_input

    def parse(self):
        """parse user input to get a simple place"""
        for regex in PARSE_REGEX:
            parse = re.search(regex, self.user_input)

            if parse:
                parse = parse.group(2)
                return parse

    def address(self):
        """use the simple place to get an address"""
        pass

    def info(self):
        """use the address to get some data from the wiki"""
        pass

    def answer(self):
        """format the answer given by the wiki"""
        return "WIP"
