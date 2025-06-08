from abc import ABC, abstractmethod
from typing import Union, Optional


class IRowParser(ABC):

    @abstractmethod
    def get_country_name(self, row: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_population(self, row: str) -> Union[int, float]:
        raise NotImplementedError

    @abstractmethod
    def get_region(self, row: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_subregion(self, row: str) -> Optional[str]:
        raise NotImplementedError
