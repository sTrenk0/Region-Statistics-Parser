from region_parser.domain.interfaces.factory import IFactory
from region_parser.domain.parser import GenericParser
from region_parser.infrastructure.db.repository import Repository

from .config import soruce_url
from .connector import StatisticsTimesConnector
from .iterator import StatisticsTimesIteratorParser
from .model import StatisticsTimesModel
from .row import StatisticsTimesRowParser
from .table import StatisticsTimesTableParser


class StatisticsTimesFactory(IFactory):

    @classmethod
    def get_parser(cls):
        return GenericParser

    @classmethod
    def get_connector(cls):
        return StatisticsTimesConnector(source_url=soruce_url)

    @classmethod
    def get_table_parser(cls):
        return StatisticsTimesTableParser()

    @classmethod
    def get_row_parser(cls):
        return StatisticsTimesRowParser()

    @classmethod
    def get_iterator_row_parser(cls):
        return StatisticsTimesIteratorParser()

    @classmethod
    def get_repository(cls):
        return Repository(StatisticsTimesModel)
