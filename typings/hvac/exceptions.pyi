class VaultError(Exception):
    def __init__(self, message: str | None = None, errors: list[str] | None = None) -> None:
        raise NotImplementedError()
