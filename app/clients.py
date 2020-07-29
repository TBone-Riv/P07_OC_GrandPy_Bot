from requests import get
import os


class Request:
    """ Handle request to API """
    @staticmethod
    def place_search(user_input: str):
        """ Use a string to get an address from Place Search """
        url = "https://maps.googleapis.com/maps/" +\
              "api/place/findplacefromtext/json?"
        output = {
            "input": user_input,
            "fields": "formatted_address,name,geometry",
            "inputtype": "textquery",
            "key": os.environ.get("GOOGLE_KEY")
        }
        res = get(url, params=output)

        if res.status_code != 200:
            raise ConnectionError()
        return res.json()

    @staticmethod
    def wiki_url(search: str):
        url = "https://fr.wikipedia.org/w/api.php?"
        params = {
            "action": "opensearch",
            "format": "json",
            "search": search
        }
        res = get(url, params=params)

        if res.status_code != 200:
            raise ConnectionError()

        return res.json()

    @staticmethod
    def wiki_content(search_url: str, extract=True):
        url = "https://fr.wikipedia.org/w/api.php?"

        params = {
            "action": "query",
            "prop": "extracts",
            "exsentences": 10,
            "exlimit": 1,
            "explaintext": 1,
            "titles": search_url,
            "formatversion": 2,
            "format": "json"
        }

        if not extract:
            params = {
                "action": "query",
                "prop": "revisions",
                "titles": search_url,
                "rvslots": "*",
                "rvprop": "content",
                "formatversion": 2,
                "format": "json"
            }

        res = get(url, params=params)

        if res.status_code != 200:
            raise ConnectionError()

        return res.json()
