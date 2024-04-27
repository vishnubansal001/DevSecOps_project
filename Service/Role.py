from Model.role import CreateRole,RetrieveRole
from Repository.Database import Database
from fastapi import HTTPException


class RoleService(Database):
    def __init__(self):
        super().__init__()

    async def get_roles(self):
        return await self.get_all("role")

    async def get_role(self, identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await self.get_one("role", identifier)
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result

    async def create(self,role: CreateRole):
        if role is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.add_item("role", role.dict()) 

    async def update(self,role: RetrieveRole):
        if role is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("role", role.identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.update_one("role", role.identifier, role.dict())
    
    async def delete(self,identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("role", identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.delete_one("role", identifier)