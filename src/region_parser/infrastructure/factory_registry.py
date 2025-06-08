from typing import Type

from region_parser.domain.interfaces.factory import IFactory


class FactoryRegistry:

    def __init__(self):
        self.factories = {}

    def _validate(self, source_name: str):
        if source_name not in self.factories:
            raise ValueError(f"Source with name: {source_name}, is not registered")

    def register(self, source_name: str, factory: Type[IFactory]):
        self.factories[source_name] = factory

    def get_factory(self, source_name: str) -> Type[IFactory]:
        self._validate(source_name)
        return self.factories[source_name]


factory_registry = FactoryRegistry()
