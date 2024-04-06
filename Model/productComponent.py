from pydantic import BaseModel

class CreateProductComponent(BaseModel):
    product: int
    component: int

class RetrieveProductComponent(BaseModel):
    identifier: int
    product: int
    component: int