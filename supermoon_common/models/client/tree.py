from pydantic import BaseModel
from supermoon_common.models.client.dirlist import DirlistEntry


class TreeDirEntry(DirlistEntry):
    children: list['TreeDirEntry'] | None


class TreeResponse(BaseModel):
    __root__: list[TreeDirEntry]
