from Model.productHistory import CreateProductHistory,RetrieveProductHistory
from Config.Connection import prisma_connection
from fastapi import HTTPException

class ProductHistoryRepository:

    @staticmethod
    async def get_product_histories():
        return await prisma_connection.prisma.productHistory.find_many()

    @staticmethod
    async def get_product_history(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await prisma_connection.prisma.productHistory.find_first(where={"identifier": identifier})
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result
    
    @staticmethod
    async def create(productHistory: CreateProductHistory):
        if productHistory is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.productHistory.create({
            "product": productHistory.product,
            "created": productHistory.created,
            "operator": productHistory.operator,
            "previousVersion": productHistory.previousVersion,
            "previousStatus": productHistory.previousStatus
        })
    
    @staticmethod
    async def update(productHistory: RetrieveProductHistory):
        if productHistory is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.productHistory.find_first(where={"identifier": productHistory.identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.productHistory.update({
            where: {"identifier": productHistory.identifier},
            data: {
                "product": productHistory.product,
                "created": productHistory.created,
                "operator": productHistory.operator,
                "previousVersion": productHistory.previousVersion,
                "previousStatus": productHistory.previousStatus
            }
        })
    
    @staticmethod
    async def delete(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.productHistory.find_first(where={"identifier": identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.productHistory.delete(where={"identifier": identifier})