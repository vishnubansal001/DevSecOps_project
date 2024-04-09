from pydantic import BaseModel

class CreateOperatorRole(BaseModel):
    operator: int
    role: int

class RetrieveOperatorRole(BaseModel):
    identifier: int
    operator: int
    role: int