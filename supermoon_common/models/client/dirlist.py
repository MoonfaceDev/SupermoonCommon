from pydantic import BaseModel
from typing import Literal


DirlistEntryType = Literal['file', 'dir', 'symlink']


class DirlistEntry(BaseModel):
    name: str
    type: DirlistEntryType
    mode: int
    owner: int
    group: int
    device: int
    access_time: float
    modification_time: float
    creation_time: float
    size: int


class DirlistResponse(BaseModel):
    __root__: list[DirlistEntry]
