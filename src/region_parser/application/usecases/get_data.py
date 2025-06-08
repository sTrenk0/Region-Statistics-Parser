from region_parser.domain.interfaces.factory import IFactory


class GetDataUseCase:

    def __init__(
            self,
            factory: IFactory,
    ):
        self._factory = factory

    async def execute(self):
        parser = self._factory.get_parser()
        parsed_countries = parser(
            connector=self._factory.get_connector(),
            iterable=self._factory.get_iterator_row_parser(),
            row=self._factory.get_row_parser(),
            table=self._factory.get_table_parser(),
        ).parse()
        repository = self._factory.get_repository()
        await repository.save_countries(parsed_countries)
