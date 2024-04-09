from pydantic import BaseModel

class CreateRequest(BaseModel):
    release: int
    created: int
    status: str
    documentation: str

class RetrieveRequest(BaseModel):
    identifier: int
    release: int
    created: int
    status: str
    documentation: str