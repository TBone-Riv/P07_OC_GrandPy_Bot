import pytest
from unittest import mock
import app.models as models
from app.tests.config import parse_sample, address_sample,\
    parse_address, info_sample


# test parse_question
@pytest.mark.parametrize("test_input,expected", parse_sample)
def test_parse(test_input, expected):
    assert models.Question("").parse_question(test_input) == expected


def test_parse_null():
    test = """j'aime le code"""
    assert not models.Question("").parse_question(test)


# test get_address
@pytest.mark.parametrize("test_input,mock_value,expected", address_sample)
def test_get_address(test_input, mock_value, expected):
    with mock.patch("app.models.Request.place_search",
                    return_value=mock_value):
        assert models.Question("").get_address(test_input) == expected


# test parse_address
@pytest.mark.parametrize("test_input,expected", parse_address)
def parse_parse_address(test_input, mock_value, expected):
    assert models.Question("").parse_address("", test_input) == expected


# test get_info
@pytest.mark.parametrize("test_input,mock_value,expected", info_sample)
def test_get_info(test_input, mock_value, expected):
    with mock.patch("app.models.random.choice",
                    return_value=test_input):
        with mock.patch("app.models.Request.place_search",
                        return_value=mock_value):
            assert models.Question("").get_info("") == expected
