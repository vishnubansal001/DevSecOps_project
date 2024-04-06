from pydantic import BaseModel

class CreateRole(BaseModel):
    role: str

class RetrieveRole(BaseModel):
    identifier: int
    role: str