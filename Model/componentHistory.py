from pydantic import BaseModel

class CreateComponentHistory(BaseModel):
    component: int
    created: int
    operator: int
    previousVersion: str
    previousReleaseStatus: str

class RetrieveComponentHistory(BaseModel):
    identifier: int
    component: int
    created: int
    operator: int
    previousVersion: str
    previousReleaseStatus: str