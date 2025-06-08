from typing import List

from region_parser.domain.entities import Country
from region_parser.domain.interfaces.parser import IParser
from region_parser.domain.interfaces.parser_components.connector import IConnector
from region_parser.domain.interfaces.parser_components.iterator_row import IIteratorRowParser
from region_parser.domain.interfaces.parser_components.row import IRowParser
from region_parser.domain.interfaces.parser_components.table import ITableParser


class GenericParser(IParser):

    def __init__(self, iterable: IIteratorRowParser, row: IRowParser, table: ITableParser, connector: IConnector):
        super().__init__(connector, iterable, row, table)

        self.parsed_countries = []

    def parse(self) -> List[Country]:
        html = self.connector.get_source_html()
        table = self.table.get_table(html)
        for row in self.iterable(table):
            self.parsed_countries.append(
                Country(
                    country_name=self.row.get_country_name(row),
                    population=self.row.get_population(row),
                    region=self.row.get_region(row),
                    subregion=self.row.get_subregion(row),
                )
            )

        return self.parsed_countries
