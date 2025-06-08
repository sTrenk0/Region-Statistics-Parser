import pathlib
import sys
from typing import Type

from tortoise import Tortoise

from .model import BaseModel


def _format_path_as_relative(path: str) -> str:
    root = pathlib.Path(__file__).parent.parent.parent
    relative_path = pathlib.Path(path).relative_to(root)
    return f"{root.name}.{relative_path}".replace(".py", "").replace("/", ".")


class _DatabaseCore:

    def __init__(
            self,
            model: Type[BaseModel],
            db_name: str,
            db_user: str,
            db_password: str,
            db_host: str,
            db_port: int,
    ):
        self.model = model
        self.connection_url = f"postgres://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    async def _connect(self) -> None:
        await Tortoise.init(
            db_url=self.connection_url,
            modules={
                "models": [
                    _format_path_as_relative(
                        sys.modules[self.model.__module__].__file__
                    )
                ]
            },
        )

    async def _cleanup(self) -> None:
        await self.model.all().delete()

    @staticmethod
    async def _generate_schemas() -> None:
        await Tortoise.generate_schemas()

    async def setup(self, cleanup: bool = False) -> None:
        await self._connect()
        await self._generate_schemas()
        if cleanup:
            await self._cleanup()


async def setup_db(
        model: Type[BaseModel],
        db_name: str,
        db_user: str,
        db_password: str,
        db_host: str,
        db_port: int,
        cleanup: bool = False
):
    await _DatabaseCore(
        model,
        db_name,
        db_user,
        db_password,
        db_host,
        db_port
    ).setup(cleanup=cleanup)
