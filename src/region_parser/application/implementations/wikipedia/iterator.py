from typing import Iterator

import bs4
from region_parser.application.utils import get_soup
from region_parser.domain.interfaces.parser_components.iterator_row import IIteratorRowParser


class WikipediaIteratorParser(IIteratorRowParser):

    def __call__(self, table: str) -> Iterator[str]:
        soup = get_soup(table)
        return self._iter_rows(soup)

    @staticmethod
    def _iter_rows(soup: bs4.Tag) -> Iterator[str]:
        rows = iter(soup.find("tbody").children)
        skipped = 0
        while True:
            try:
                row = next(rows)
            except StopIteration:
                break
            if row.name != "tr":
                continue
            if skipped != 2:
                skipped += 1
                continue
            yield row.__str__()
