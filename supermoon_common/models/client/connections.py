from pydantic import BaseModel


class Address(BaseModel):
    host: str
    port: int


class Connection(BaseModel):
    family: str
    type: str
    pid: int
    status: str
    local_address: str | Address | None
    remote_address: str | Address | None


class ConnectionsResponse(BaseModel):
    __root__: list[Connection]
