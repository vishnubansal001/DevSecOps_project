from pydantic import BaseModel

class CreateComponentHistory(BaseModel):
    component: int
    created: int
    operator: int
    previousVersion: str
    previousStatus: str

class RetrieveComponentHistory(BaseModel):
    identifier: int
    component: int
    created: int
    operator: int
    previousVersion: str
    previousStatus: str