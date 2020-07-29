import random
import re
from config import PARSE_REGEX, ADDRESS_REGEX,\
    STRING_ERROR_PARSE, STRING_ERROR_ADDRESS,\
    STRING_ERROR_WIKI
from app.clients import Request


class Question:
    def __init__(self, user_input: str):
        self.user_input = user_input
        self.parse_input = None
        self.new_parse = None
        self.address = None
        self.geometry = None
        self.list_search = None
        self.searched_string = None
        self.wiki_content = None
        self.url = None

    @staticmethod
    def parse_question(string):
        """parse user input to get a simple place"""
        for regex in PARSE_REGEX:
            parse = re.search(regex, string)

            if parse:
                parse = parse.group(2)
                return parse

    @staticmethod
    def get_address(string_parse):
        """use the simple place to get an address"""
        if not string_parse:
            return None, None

        response = Request.place_search(string_parse)

        if not response["candidates"]:
            return None, None, {"lat": 0, "lng": 0}

        address = response["candidates"][0]

        new_parse = address["name"]

        geometry = address["geometry"]["location"]

        return new_parse, address["formatted_address"], geometry

    @staticmethod
    def parse_address(parse, address_string):

        list_wiki = [parse]
        element_address = [e.strip() for e in address_string.split(',')]
        element_address[-2] = element_address[-2].split(' ')[-1]

        for index, _ in enumerate(element_address):
            for regex in ADDRESS_REGEX:
                parse_address = re.search(regex, element_address[index])

                if parse_address:
                    element_address[index] = parse_address.group(2)
                    break

        list_wiki.extend(element_address)

        return list_wiki

    @staticmethod
    def get_info(list_wiki):
        """choose a element in the list to get some data from the wiki"""

        search = random.choice(list_wiki)

        data = Request.wiki_url(search)

        list_data = data[1]
        list_url = data[3]

        if not len(list_data):
            return search, None, None

        index = 0

        search = list_data[index]
        url = list_url[index]
        string_url = url.split("/")
        string_url = string_url[-1]
        data = Request.wiki_content(string_url)

        content = data["query"]["pages"][0].get("extract")

        if not content:
            data = Request.wiki_content(string_url, extract=False)
            content = data["query"]["pages"][0].get("revisions")
            if not content:
                return search, None, url

            content = content["content"]
            content = content.split("\n\n''")[1]
            content = content.replace('[[', '')
            content = content.replace(']]', '')
            content = content.replace('{{', '')
            content = content.replace('}}', '')
            content = content.replace("''", '')
            content = content.replace("Date|", '')
            content = content.replace("date-|", '')
            content = content.replace("|", ' ')

            content = re.search(r"^.{1,1300}[^\s].\.", content).group()

        content = "<p>" + content.replace("\n", "</p><p>") + "</p>"

        return search, content, url

    def answer(self):
        """format the answer given by the wiki"""

        user_input = self.user_input

        self.parse_input = self.parse_question(user_input)
        if not self.parse_input:
            self.parse_input = "???"
            self.new_parse = "???"
            self.address = "???"
            self.list_search = ["???"]
            self.searched_string = "???"
            self.wiki_content = STRING_ERROR_PARSE

            title = "Grampy n'a pas comprit"
            info = "<p>:/</p>"

        else:

            self.new_parse, self.address, self.geometry = \
                self.get_address(self.parse_input)

            if not self.new_parse or not self.address:
                self.wiki_content = STRING_ERROR_ADDRESS

                title = self.parse_input + " n'est pas sur la carte"
                info = "<p>:/</p>"

            else:

                self.list_search = self.parse_address(self.new_parse,
                                                      self.address)

                self.searched_string, self.wiki_content, self.url =\
                    self.get_info(self.list_search)

                if not self.wiki_content:
                    self.wiki_content = STRING_ERROR_WIKI
                    self.url = ''

                title = "Ce que Grampy sait sur '" + self.new_parse + "' :"

                info = "<p>Adresse : " + self.address + "</p>" +\
                    "<p>Recherche possible : " +\
                    ", ".join(self.list_search) + "</p>" +\
                    "<p>Recherche faite sur : <a href=\"" +\
                    self.url + "\">" + self.searched_string + "</a></p>"

        content = "<p>" + self.wiki_content + "</p>"

        answer = {
            "title": title,
            "info": info,
            "content": content,
            "geometry": self.geometry
        }

        return answer
