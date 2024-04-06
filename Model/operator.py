from pydantic import BaseModel

class CreateOperator(BaseModel):
    name: str

class RetrieveOperator(BaseModel):
    identifier: int
    name: str