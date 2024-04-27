from Model.operator import CreateOperator,RetrieveOperator
from Repository.Database import Database
from fastapi import HTTPException


class OperatorService(Database):
    def __init__(self):
        super().__init__()

    async def get_operators(self):
        return await self.get_all("operator")

    async def get_operator(self, identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await self.get_one("operator", identifier)
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result
        

    async def create(self, operator: CreateOperator):
        if operator is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.add_item("operator", operator.dict())

    async def update(self, operator: RetrieveOperator):
        if operator is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("operator", operator.identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.update_one("operator", operator.identifier, operator.dict())
    
    async def delete(self,identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("operator", identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.delete_one("operator", identifier)