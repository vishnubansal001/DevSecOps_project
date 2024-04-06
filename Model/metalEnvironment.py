from pydantic import BaseModel

class CreateMetalEnvironment(BaseModel):
    metal: int
    environment: int

class RetrieveMetalEnvironment(BaseModel):
    identifier: int
    metal: int
    environment: int