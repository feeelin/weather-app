from dataclasses import dataclass


@dataclass
class Session:
    base_url: str
    headers: dict


class HttpClient:
    def __init__(self, base_url: str, api_key: str) -> None:
        self._session = Session(base_url=base_url, headers={'appid': api_key})
