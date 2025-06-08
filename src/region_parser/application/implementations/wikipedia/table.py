from region_parser.application.utils import get_soup
from region_parser.domain.interfaces.parser_components.table import ITableParser


class WikipediaTableParser(ITableParser):

    def get_table(self, html: str) -> str:
        soup = get_soup(html)
        return soup.find(
            "table",
            {
                "class": "wikitable",
            },
        ).find("tbody").__str__()
