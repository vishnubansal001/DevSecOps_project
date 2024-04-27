from pydantic import BaseModel

class CreateComponent(BaseModel):
    created: int
    fullName: str
    shortName: str
    version: str
    configuration: int
    containerimagetag: str

class RetrieveComponent(BaseModel):
    identifier: int
    created: int
    fullName: str
    shortName: str
    version: str
    configuration: int
    containerimagetag: str