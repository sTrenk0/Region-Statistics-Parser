from abc import ABC, abstractmethod


class ITableParser(ABC):

    @abstractmethod
    def get_table(self, html: str) -> str:
        raise NotImplementedError
