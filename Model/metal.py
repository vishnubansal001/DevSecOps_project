from pydantic import BaseModel

class CreateMetal(BaseModel):
    fullName: str
    shortName: str
    configuration: int

class RetrieveMetal(BaseModel):
    identifier: int
    fullName: str
    shortName: str
    configuration: int