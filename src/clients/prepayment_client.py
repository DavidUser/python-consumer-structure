from pydantic import BaseModel

from clients.base_client import BaseClient


class ResponseBlah(BaseModel):
    id: int


class PrepaymentClient(BaseClient):
    def create_blah(self) -> ResponseBlah:
        pass
