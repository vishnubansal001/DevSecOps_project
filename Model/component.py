from pydantic import BaseModel

class CreateComponent(BaseModel):
    created: int
    fullName: str
    shortName: str
    version: str
    configuration: int
    status: str

class RetrieveComponent(BaseModel):
    identifier: int
    created: int
    fullName: str
    shortName: str
    version: str
    configuration: int
    status: str