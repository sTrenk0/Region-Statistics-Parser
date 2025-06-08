from typing import Callable, ParamSpec, TypeVar

import click

from .config import default_config
from .infrastructure.factory_registry import factory_registry

P = ParamSpec("P")
T = TypeVar("T")


def get_sources() -> tuple[str, ...]:
    return tuple(map(lambda k: k.lower(), factory_registry.factories.keys()))


def show_sources(ctx: click.Context, param: click.Parameter, value: bool) -> None:
    if not value or ctx.resilient_parsing:
        return
    click.echo(
        "Right now, only such resources are available for parsing: " + "["
        + ", ".join(get_sources()) + "]"
    )
    ctx.exit()


def common_options(f: Callable[P, T]) -> Callable[P, T]:
    """Decorator to apply common CLI options."""
    options = [
        click.argument(
            "source",
            envvar="SOURCE",
            type=click.Choice(get_sources(), case_sensitive=False),
            default=default_config["source"],
        ),
        click.option(
            "--db-user",
            "db_user",
            default=default_config["db_user"],
            type=str,
            envvar="DB_USER",
            help="Database user name",
            show_default=True,
        ),
        click.option(
            "--db-password",
            "db_password",
            default=default_config["db_password"],
            type=str,
            envvar="DB_PASSWORD",
            help="Database user password",
        ),
        click.option(
            "--db-host",
            "db_host",
            default=default_config["db_host"],
            help="Database host",
            type=str,
            envvar="DB_HOST",
            show_default=True,
        ),
        click.option(
            "--db-port",
            "db_port",
            default=default_config["db_port"],
            type=int,
            envvar="DB_PORT",
            help="Database port",
            show_default=True,
        ),
        click.option(
            "--db-name",
            "db_name",
            default=default_config["db_name"],
            type=str,
            envvar="DB_NAME",
            help="Database name",
            show_default=True,
        ),
        click.option(
            "--sources",
            is_eager=True,
            is_flag=True,
            callback=show_sources,
            help="Show available sources",
            expose_value=False,
        ),
    ]
    for option in reversed(options):
        f = option(f)
    return f
