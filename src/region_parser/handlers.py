import logging
import sys

import click

from .application.exceptions import BaseAppException
from .application.usecases.get_data import GetDataUseCase
from .application.usecases.print_data import PrintDataUseCase
from .infrastructure.factory_registry import factory_registry

errors = logging.getLogger("errors")
access = logging.getLogger("access")


async def _get_data_handler(source: str):
    factory = factory_registry.get_factory(source)
    try:
        try:
            await GetDataUseCase(factory).execute()
            click.echo("Data parsed successfully")
        except (AssertionError, BaseAppException) as client_exception:
            click.echo(client_exception)
            sys.exit(1)

    except Exception as e:
        click.echo("An error occurred, see the error logs")
        errors.exception(e)
        sys.exit(1)


async def _print_data_handler(source: str):
    factory = factory_registry.get_factory(source)
    try:
        try:
            results = await PrintDataUseCase(factory).execute()
            for result in results:
                click.echo(
                    f"""
                                Region: {result.region}
                    _________________________________________________
                    Total population in region: {result.total_population}
                    Largest Country: {result.max_country_name}
                    Largest Country Population: {result.max_population}
                    Smallest Country: {result.min_country_name}
                    Smallest Country Population: {result.min_population}
                    _________________________________________________
                    """
                )
        except (AssertionError, BaseAppException) as client_exception:
            click.echo(client_exception)
            sys.exit(1)

    except Exception as e:
        click.echo("An error occurred, see the error logs")
        errors.exception(e)
        sys.exit(1)
