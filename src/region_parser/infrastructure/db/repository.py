import asyncio
from typing import Type, List

from region_parser.domain.entities import Country, CountryStats
from region_parser.domain.interfaces.repository import IRepository

from .model import BaseModel


class Repository(IRepository):

    def __init__(self, model: Type[BaseModel]):
        self.model = model
        self._pending_tasks = []

    async def save_country(self, country: Country):
        country = await self.model(
            country_name=country.country_name,
            population=country.population,
            region=country.region,
            subregion=country.subregion
        )
        await country.save()

    async def save_countries(self, countries: List[Country]):
        tasks = [self.save_country(country) for country in countries]
        await asyncio.gather(*tasks)

    async def get_region_stats(self) -> List[CountryStats]:
        query = f"""
                SELECT
                    region,
                    SUM(population) AS total_population,
                    MAX(country_name) FILTER (WHERE population = max_pop) AS max_country_name,
                    MAX(population) AS max_population,
                    MIN(country_name) FILTER (WHERE population = min_pop) AS min_country_name,
                    MIN(population) AS min_population
                FROM (
                    SELECT
                        *,
                        MAX(population) OVER (PARTITION BY region) AS max_pop,
                        MIN(population) OVER (PARTITION BY region) AS min_pop
                    FROM {self.model._meta.db_table}
                ) AS ranked
                GROUP BY region;
                """

        conn = self.model._meta.db
        result = await conn.execute_query_dict(query)
        return [CountryStats(**r) for r in result]

    def get_model(self) -> Type[BaseModel]:
        return self.model
