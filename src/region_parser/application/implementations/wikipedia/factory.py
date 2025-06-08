from region_parser.domain.interfaces.factory import IFactory
from region_parser.domain.parser import GenericParser
from region_parser.infrastructure.db.repository import Repository

from .config import soruce_url
from .connector import WikipediaConnector
from .iterator import WikipediaIteratorParser
from .model import WikipediaModel
from .row import WikipediaRowParser
from .table import WikipediaTableParser


class WikipediaFactory(IFactory):

    @classmethod
    def get_parser(cls):
        return GenericParser

    @classmethod
    def get_connector(cls):
        return WikipediaConnector(source_url=soruce_url)

    @classmethod
    def get_table_parser(cls):
        return WikipediaTableParser()

    @classmethod
    def get_row_parser(cls):
        return WikipediaRowParser()

    @classmethod
    def get_iterator_row_parser(cls):
        return WikipediaIteratorParser()

    @classmethod
    def get_repository(cls):
        return Repository(WikipediaModel)
