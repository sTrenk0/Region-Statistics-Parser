from abc import ABC, abstractmethod
from typing import Type

from .parser import IParser
from .parser_components.connector import IConnector
from .parser_components.iterator_row import IIteratorRowParser
from .parser_components.row import IRowParser
from .parser_components.table import ITableParser
from .repository import IRepository


class IFactory(ABC):

    @classmethod
    @abstractmethod
    def get_connector(cls) -> IConnector:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_parser(cls) -> Type[IParser]:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_iterator_row_parser(cls) -> IIteratorRowParser:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_row_parser(cls) -> IRowParser:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_table_parser(cls) -> ITableParser:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_repository(cls) -> IRepository:
        raise NotImplementedError
