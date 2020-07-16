import pytest
import app.models as models


# test parse
parse_sample = [
    ("""Que peut tu me dire sur l'école de Nante ?""",
     """l'école de Nante"""),
    ("""parle moi du puy du fou""",
     """puy du fou"""),
    ("""Done moi l'adresse d'Openclassrooms stp""",
     """Openclassrooms"""),
    ("""raconte moi une histoire sur la gare de Lyon s'il te plait""",
     """la gare de Lyon""")]


@pytest.mark.parametrize("test_input,expected", parse_sample)
def test_parse(test_input, expected):
    assert models.Question(test_input).parse() == expected


def test_parse_null():
    test = """j'aime le code"""
    assert not models.Question(test).parse()

