# Region Parser

**Region Parser** is an asynchronous Python application designed to automatically collect and analyze country and region
data from various online sources.  
The project is easily extendable with additional sources and fully configurable via environment variables.

## Features

- Parses country data from supported sources (`wikipedia`, `statisticstimes`).
- Stores data in PostgreSQL using **Tortoise ORM**.
- Executes aggregated SQL queries (e.g., total regional population, largest/smallest country).

## Configuration via Environment Variables

All database connection and parsing settings are configurable via `.env` or `docker-compose.yml`:

| Variable       | Description       | Default Value |
|----------------|-------------------|---------------|
| `DB_HOST_NAME` | Database host     | `postgres`    |
| `DB_PORT`      | Database port     | `5432`        |
| `DB_USER`      | Database user     | `postgres`    |
| `DB_PASSWORD`  | Database password | `postgres`    |
| `DB_NAME`      | Database name     | `postgres`    |
| `SOURCE`       | Parsing source    | `wikipedia`   |

Example Docker usage for collecting data:

```bash
docker compose up get_data
```

Example Docker usage for printing data:

```bash
docker compose up print_data
```