from Model.operator import CreateOperator,RetrieveOperator
from Config.Connection import prisma_connection
from fastapi import HTTPException

class OperatorRepository:

    @staticmethod
    async def get_operators():
        return await prisma_connection.prisma.operator.find_many()

    @staticmethod
    async def get_operator(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await prisma_connection.prisma.operator.find_first(where={"identifier": identifier})
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result

    @staticmethod
    async def create(operator: CreateOperator):
        if operator is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.operator.create({
            "name": operator.name
        })

    @staticmethod
    async def update(operator: RetrieveOperator):
        if operator is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.operator.find_first(where={"identifier": operator.identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.operator.update({
            where: {"identifier": operator.identifier},
            data: {
                "name": operator.name
            }
        })
    
    @staticmethod
    async def delete(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.operator.find_first(where={"identifier": identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.operator.delete(where={"identifier": identifier})