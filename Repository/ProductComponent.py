from Model.productComponent import CreateProductComponent,RetrieveProductComponent
from Config.Connection import prisma_connection
from fastapi import HTTPException

class ProductComponentRepository:

    @staticmethod
    async def get_productComponents():
        return await prisma_connection.prisma.productComponent.find_many()

    @staticmethod
    async def get_productComponent(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await prisma_connection.prisma.productComponent.find_first(where={"identifier": identifier})
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result
    
    @staticmethod
    async def create(productComponent: CreateProductComponent):
        if productComponent is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.productComponent.create({
            "product": productComponent.product,
            "component": productComponent.component
        })
    
    @staticmethod
    async def update(productComponent: RetrieveProductComponent):
        if productComponent is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.productComponent.find_first(where={"identifier": productComponent.identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.productComponent.update({
            where: {"identifier": productComponent.identifier},
            data: {
                "product": productComponent.product,
                "component": productComponent.component
            }
        })
    
    @staticmethod
    async def delete(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.productComponent.find_first(where={"identifier": identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.productComponent.delete(where={"identifier": identifier})