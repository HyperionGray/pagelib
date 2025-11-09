"""
HtmlPage tests.
"""
import pathlib
import pytest

# Pagelib
from pagelib import HtmlPage


_FIXTURE_PATH = pathlib.Path(__file__).parent.joinpath('fixtures')


class PagelibTestException(Exception):
    """
    Pagelib test exception.
    """
    pass


@pytest.fixture
def html_page():
    """
    Returns an HtmlPage instance with html loaded from the fixtures
    directory.
    """
    with open(str(_FIXTURE_PATH.joinpath('index.html'))) as f:
        html = f.read()
        return HtmlPage(html)
    raise PagelibTestException('Could not load html from {}'.format(_FIXTURE_PATH))


def test_title(html_page):
    assert html_page.title == 'Welcome to Python.org'


def test_meta_description(html_page):
    assert html_page.meta_description == 'The official home of the Python Programming Language'


def test_meta_keywords(html_page):
    assert html_page.meta_keywords == 'Python programming language object oriented web ' \
                                      'free open source software license documentation ' \
                                      'download community'


def test_language_code(html_page):
    assert html_page.language_code == 'en'


def test_language_name(html_page):
    assert html_page.language_name == 'English'


def test_words_is_list(html_page):
    assert isinstance(html_page.words, list)


def test_words_count(html_page):
    assert len(html_page.words) == 944


def test_sentences_is_list(html_page):
    assert isinstance(html_page.sentences, list)


def test_sentence_count(html_page):
    assert len(html_page.sentences) == 366


def test_text_is_str(html_page):
    assert isinstance(html_page.text, str)


def test_text_length(html_page):
    assert len(html_page.text) == 16598


def test_size(html_page):
    assert html_page.bytes == 48170
