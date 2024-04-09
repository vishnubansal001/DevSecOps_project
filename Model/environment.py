from pydantic import BaseModel

class CreateEnvironment(BaseModel):
    fullName: str
    shortName: str
    configuration: int

class RetrieveEnvironment(BaseModel):
    identifier: int
    fullName: str
    shortName: str
    configuration: int