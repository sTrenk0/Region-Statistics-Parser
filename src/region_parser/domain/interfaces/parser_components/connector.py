from abc import ABC, abstractmethod


class IConnector(ABC):

    @abstractmethod
    def get_source_html(self) -> str:
        raise NotImplementedError
