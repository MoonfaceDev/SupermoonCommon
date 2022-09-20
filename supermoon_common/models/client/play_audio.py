from pydantic import BaseModel


class PlayAudioBufferRequest(BaseModel):
    type: str
    data: str  # base 64
