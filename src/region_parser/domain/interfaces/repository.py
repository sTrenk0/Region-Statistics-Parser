from abc import ABC, abstractmethod
from typing import Any, List

from ..entities import Country, CountryStats


class IRepository(ABC):
    @abstractmethod
    async def save_country(self, country: Country):
        raise NotImplementedError

    @abstractmethod
    async def save_countries(self, countries: List[Country]):
        raise NotImplementedError

    @abstractmethod
    async def get_region_stats(self) -> List[CountryStats]:
        raise NotImplementedError

    @abstractmethod
    def get_model(self) -> Any:
        raise NotImplementedError
