from Model.operatorRole import CreateOperatorRole,RetrieveOperatorRole
from Config.Connection import prisma_connection
from fastapi import HTTPException

class OperatorRoleRepository:

    @staticmethod
    async def get_operatorRoles():
        return await prisma_connection.prisma.operatorRole.find_many()

    @staticmethod
    async def get_operatorRole(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await prisma_connection.prisma.operatorRole.find_first(where={"identifier": identifier})
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result
    
    @staticmethod
    async def create(operatorRole: CreateOperatorRole):
        if operatorRole is None:
            raise HTTPException(status_code=404, detail="Item not found")
        a = await prisma_connection.prisma.operator.find_first(where={"identifier": operatorRole.operator})
        if a is None:
            raise HTTPException(status_code=404, detail="Item not found")
        b = await prisma_connection.prisma.role.find_first(where={"identifier": operatorRole.role})
        if b is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.operatorRole.create({
            "operator": operatorRole.operator,
            "role": operatorRole.role
        })

    @staticmethod
    async def update(operatorRole: RetrieveOperatorRole):
        if operatorRole is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.operatorRole.find_first(where={"identifier": operatorRole.identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        a = await prisma_connection.prisma.operator.find_first(where={"identifier": operatorRole.operator})
        if a is None:
            raise HTTPException(status_code=404, detail="Item not found")
        b = await prisma_connection.prisma.role.find_first(where={"identifier": operatorRole.role})
        if b is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.operatorRole.update({
            where: {"identifier": operatorRole.identifier},
            data: {
                "operator": operatorRole.operator,
                "role": operatorRole.role
            }
        })
    
    @staticmethod
    async def delete(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.operatorRole.find_first(where={"identifier": identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.operatorRole.delete(where={"identifier": identifier})