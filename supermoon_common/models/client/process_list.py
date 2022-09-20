from typing import Any

from pydantic import BaseModel


class Process(BaseModel):
    pid: int
    memory_percent: float
    name: str
    cmdline: list[str] | None
    create_time: float
    nice: int | None
    username: str | None
    cwd: str | None
    cpu_percent: float
    num_handles: int
    environ: list[str] | Any
    ppid: int
    exe: str | None


class ProcessListResponse(BaseModel):
    __root__: list[Process]
