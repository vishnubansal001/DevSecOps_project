from Model.operatorRole import CreateOperatorRole,RetrieveOperatorRole
from Repository.Database import Database
from fastapi import HTTPException


class OperatorRoleService(Database):
    def __init__(self):
        super().__init__()

    async def get_operatorRoles(self):
        return await self.get_all("operatorRole")

    async def get_operatorRole(self, identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await self.get_one("operatorRole", identifier)
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result

    async def create(self, operatorRole: CreateOperatorRole):
        if operatorRole is None:
            raise HTTPException(status_code=404, detail="Item not found")
        a = await self.get_one("operator", operatorRole.operator)
        if a is None:
            raise HTTPException(status_code=404, detail="Item not found")
        b = await self.get_one("role", operatorRole.role)
        if b is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.add_item("operatorRole", operatorRole.dict())

    async def update(self, operatorRole: RetrieveOperatorRole):
        if operatorRole is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("operatorRole", operatorRole.identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        a = await self.get_one("operator", operatorRole.operator)
        if a is None:
            raise HTTPException(status_code=404, detail="Item not found")
        b = await self.get_one("role", operatorRole.role)
        if b is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.update_one("operatorRole", operatorRole.identifier, operatorRole.dict())
    
    async def delete(self, identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("operatorRole", identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.delete_one("operatorRole", identifier)