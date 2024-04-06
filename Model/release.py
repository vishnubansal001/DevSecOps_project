from pydantic import BaseModel

class CreateRelease(BaseModel):
    status: str
    scope: str
    effect: int
    metalEnvironment: int

class RetrieveRelease(BaseModel):
    identifier: int
    status: str
    scope: str
    effect: int
    metalEnvironment: int