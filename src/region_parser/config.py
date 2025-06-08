from typing import TypedDict

from region_parser.infrastructure.factory_registry import factory_registry

from .application.implementations.statisticstimes.factory import StatisticsTimesFactory
from .application.implementations.wikipedia.factory import WikipediaFactory


class DefaultConfig(TypedDict):
    source: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str


default_config = DefaultConfig(
    source="wikipedia",
    db_user="postgres",
    db_password="postgres",
    db_host="postgres",
    db_port=5432,
    db_name="postgres",
)

factory_registry.register("wikipedia", WikipediaFactory)
factory_registry.register("staticstimes", StatisticsTimesFactory)
