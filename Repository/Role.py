from Model.role import CreateRole,RetrieveRole
from Config.Connection import prisma_connection
from fastapi import HTTPException

class RoleRepository:

    @staticmethod
    async def get_roles():
        return await prisma_connection.prisma.role.find_many()

    @staticmethod
    async def get_role(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await prisma_connection.prisma.role.find_first(where={"identifier": identifier})
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result
    
    @staticmethod
    async def create(role: CreateRole):
        if role is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.role.create({
            "role": role.role
        })
    
    @staticmethod
    async def update(role: RetrieveRole):
        if role is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.role.find_first(where={"identifier": role.identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.role.update({
            where: {"identifier": role.identifier},
            data: {
                "role": role.role
            }
        })
    
    @staticmethod
    async def delete(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.role.find_first(where={"identifier": identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.role.delete(where={"identifier": identifier})