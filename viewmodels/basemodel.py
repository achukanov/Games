from typing import Optional

# from starlette.requests import Request

# from infrastructure import cookie_auth


class ViewModelBase:

    def __init__(self):
        self.error: Optional[str] = None

    def to_dict(self) -> dict:
        return self.__dict__
