from Model.product import CreateProduct,RetrieveProduct
from Config.Connection import prisma_connection
from fastapi import HTTPException

class ProductRepository:

    @staticmethod
    async def get_products():
        return await prisma_connection.prisma.product.find_many()
    
    @staticmethod
    async def get_product(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await prisma_connection.prisma.product.find_first(where={"identifier": identifier})
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result

    @staticmethod
    async def create(product: CreateProduct):
        if product is None:
            raise HTTPException(status_code=404, detail="Item not found")
        a = await prisma_connection.prisma.configuration.find_first(where={"identifier": product.configuration})
        if a is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.product.create({
            "fullName": product.fullName,
            "shortName": product.shortName,
            "version": product.version,
            "configuration": product.configuration,
            "status": product.status,
            "centralIntakeRequest": product.centralIntakeRequest
        })
    
    @staticmethod
    async def update(product: RetrieveProduct):
        if product is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.product.find_first(where={"identifier": product.identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        a = await prisma_connection.prisma.configuration.find_first(where={"identifier": product.configuration})
        if a is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.product.update({
            where: {"identifier": product.identifier},
            data: {
                "fullName": product.fullName,
                "shortName": product.shortName,
                "version": product.version,
                "configuration": product.configuration,
                "status": product.status,
                "centralIntakeRequest": product.centralIntakeRequest
            }
        })
    
    @staticmethod
    async def delete(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.product.find_first(where={"identifier": identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.product.delete(where={"identifier": identifier})
