from pydantic import BaseModel

class CreateConfiguration(BaseModel):
    source: str
    version: str

class RetrieveConfiguration(BaseModel):
    identifier: int
    source: str
    version: str