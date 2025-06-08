import asyncio

import click
from region_parser.commons import common_options
from region_parser.handlers import _get_data_handler, _print_data_handler
from region_parser.infrastructure.db.core import setup_db
from region_parser.infrastructure.factory_registry import factory_registry
from region_parser.log import init_logging


async def _main(handler, setup_db):
    await setup_db
    await handler


@click.group()
def cli():
    init_logging()


@cli.command(name="get-data")
@common_options
def get_data_handler(
        source: str,
        db_user: str,
        db_password: str,
        db_host: str,
        db_port: int,
        db_name: str,
):
    asyncio.run(
        _main(
            handler=_get_data_handler(source),
            setup_db=setup_db(
                factory_registry.get_factory(source).get_repository().get_model(),
                db_name,
                db_user,
                db_password,
                db_host,
                db_port,
                cleanup=True
            )
        )
    )


@cli.command(name="print-data")
@common_options
def print_data_handler(
        source: str,
        db_user: str,
        db_password: str,
        db_name: str,
        db_host: str,
        db_port: int,
):
    asyncio.run(
        _main(
            handler=_print_data_handler(source),
            setup_db=setup_db(
                model=factory_registry.get_factory(source).get_repository().get_model(),
                db_name=db_name,
                db_user=db_user,
                db_password=db_password,
                db_host=db_host,
                db_port=db_port,
                cleanup=False,
            )

        )
    )


if __name__ == "__main__":
    # cli()
    model = factory_registry.get_factory(
        "staticstimes"
    ).get_repository().get_model()

    asyncio.run(_main(
        handler=_print_data_handler(
            "staticstimes",
        ),
        setup_db=setup_db(
            model=model,
            db_name="postgres",
            db_user="postgres",
            db_password="postgres",
            db_host="localhost",
            db_port=5432,
            cleanup=False
        )
    ))
