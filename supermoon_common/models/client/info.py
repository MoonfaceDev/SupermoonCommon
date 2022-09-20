from datetime import datetime

from pydantic import BaseModel


class System(BaseModel):
    system: str
    node: str
    release: str
    version: str
    machine: str
    processor: str


class CPUFrequency(BaseModel):
    max: float
    min: float
    current: float


class CPU(BaseModel):
    physical_cores: int
    total_cores: int
    frequency: CPUFrequency
    usage: float
    core_usage: list[float]


class Memory(BaseModel):
    total: int
    available: int
    used: int
    percent: float


class PartitionUsage(BaseModel):
    total: int
    free: int
    used: int
    percent: float


class Partition(BaseModel):
    device: str
    mountpoint: str
    fstype: str
    usage: PartitionUsage


class Disk(BaseModel):
    partitions: list[Partition]
    read_bytes: int
    write_bytes: int


class NetworkAddress(BaseModel):
    family: str
    address: str
    netmask: str | None


class Network(BaseModel):
    interfaces: list[dict[str, list[NetworkAddress]]]
    bytes_sent: int
    bytes_recv: int


class Battery(BaseModel):
    percent: int
    secsleft: int
    power_plugged: int


class InfoResponse(BaseModel):
    system: System
    boot_time: datetime
    cpu: CPU
    memory: Memory
    disk: Disk
    network: Network
    battery: Battery | None
    users: list[str]
