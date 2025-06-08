import bs4
import requests

from .exceptions import CouldNotAccessSource


def get_html(source_url: str) -> str:
    with requests.Session() as session:
        with session.get(source_url) as response:
            assert (
                    response.status_code == 200
            ), CouldNotAccessSource
            return response.text


def get_soup(html: str) -> bs4.BeautifulSoup:
    return bs4.BeautifulSoup(html, "html.parser")
