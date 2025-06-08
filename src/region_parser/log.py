from logging.config import dictConfig

log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "access": {
            "level": "NOTSET",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "default",
        },
        "error": {
            "level": "ERROR",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
            "formatter": "default",
        },
    },
    "loggers": {
        "access": {
            "handlers": ["access"],
            "level": "DEBUG",
            "propagate": False,
        },
        "errors": {
            "handlers": ["error"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}


def init_logging():
    dictConfig(log_config)
