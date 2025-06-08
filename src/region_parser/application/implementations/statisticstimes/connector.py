from region_parser.application.utils import get_html
from region_parser.domain.interfaces.parser_components.connector import IConnector


class StatisticsTimesConnector(IConnector):

    def __init__(self, source_url: str):
        self.source_url = source_url

    def get_source_html(self) -> str:
        return get_html(self.source_url)
