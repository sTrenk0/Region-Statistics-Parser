from typing import List

from region_parser.domain.entities import CountryStats
from region_parser.domain.interfaces.factory import IFactory


class PrintDataUseCase:

    def __init__(
            self,
            factory: IFactory,
    ):
        self._factory = factory

    async def execute(self) -> List[CountryStats]:
        repository = self._factory.get_repository()
        return await repository.get_region_stats()
