from typing import Optional

from region_parser.application.utils import get_soup
from region_parser.domain.interfaces.parser_components.row import IRowParser


class StatisticsTimesRowParser(IRowParser):

    def get_country_name(self, row: str) -> str:
        soup = get_soup(row)
        fields = soup.find_all("td")
        return fields[0].find("a").text.strip()

    def get_population(self, row: str) -> Optional[int]:
        soup = get_soup(row)
        fields = soup.find_all("td")
        value = fields[1].text.strip().replace(",", "")
        if value.isdigit():
            return int(value)
        return None

    def get_region(self, row: str) -> str:
        soup = get_soup(row)
        fields = soup.find_all("td")
        return fields[-1].text.strip()

    def get_subregion(self, row: str) -> None:
        return None
