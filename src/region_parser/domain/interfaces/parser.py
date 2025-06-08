from abc import ABC, abstractmethod
from typing import List

from region_parser.domain.entities import Country
from region_parser.domain.interfaces.parser_components.connector import IConnector
from region_parser.domain.interfaces.parser_components.iterator_row import IIteratorRowParser
from region_parser.domain.interfaces.parser_components.row import IRowParser
from region_parser.domain.interfaces.parser_components.table import ITableParser


class IParser(ABC):

    def __init__(
            self,
            connector: IConnector,
            iterable: IIteratorRowParser,
            row: IRowParser,
            table: ITableParser
    ):
        self.connector = connector
        self.iterable = iterable
        self.row = row
        self.table = table

    @abstractmethod
    def parse(self) -> List[Country]:
        raise NotImplementedError
