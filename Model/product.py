from pydantic import BaseModel

class CreateProduct(BaseModel):
    fullName: str
    shortName: str
    version: str
    configuration: int
    centralIntakeRequest: str

class RetrieveProduct(BaseModel):
    identifier: int
    fullName: str
    shortName: str
    version: str
    configuration: int
    centralIntakeRequest: str