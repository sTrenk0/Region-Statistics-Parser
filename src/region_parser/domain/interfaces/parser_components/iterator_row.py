from abc import abstractmethod, ABC
from typing import Iterator


class IIteratorRowParser(ABC):

    @abstractmethod
    def __call__(self, table: str) -> Iterator[str]:
        raise NotImplementedError
