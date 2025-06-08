class BaseAppException(Exception):

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return self.message


class CouldNotAccessSource(BaseAppException):

    def __init__(self):
        super().__init__(
            """
            Could not access the url,
            check if the url string contains an error,
            or try again later.
            """
        )
