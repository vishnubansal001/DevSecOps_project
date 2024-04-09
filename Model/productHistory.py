from pydantic import BaseModel

class CreateProductHistory(BaseModel):
    product: int
    created: int
    operator: int
    previousVersion: str
    previousStatus: str

class RetrieveProductHistory(BaseModel):
    identifier: int
    product: int
    created: int
    operator: int
    previousVersion: str
    previousStatus: str