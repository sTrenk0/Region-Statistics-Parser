from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Country:
    country_name: str
    population: int
    region: str
    subregion: Optional[str] = field(default=None)


@dataclass
class CountryStats:
    region: str
    total_population: int
    max_country_name: str
    max_population: int
    min_country_name: str
    min_population: int
