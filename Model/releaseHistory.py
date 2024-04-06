from pydantic import BaseModel

class CreateReleaseHistory(BaseModel):
    release: int
    created: int
    operator: int
    previousStatus: str

class RetrieveReleaseHistory(BaseModel):
    identifier: int
    release: int
    created: int
    operator: int
    previousStatus: str