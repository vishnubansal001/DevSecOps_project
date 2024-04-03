from Model.product import CreateProduct
from Config.Connection import prisma_connection

class ProductRepository:

    @staticmethod
    async def get_products():
        return await prisma_connection.product.find_many()
    
    @staticmethod
    async def get_product(identifier: int):
        return await prisma_connection.product.find_first(where={"identifier": identifier})

    @staticmethod
    async def create(product: CreateProduct):
        return await prisma_connection.product.create({
            "fullName": product.fullName,
            "shortName": product.shortName,
            "version": product.version,
            "configuration": product.configuration,
            "status": product.status,
            "centralIntakeRequest": product.centralIntakeRequest
        })
    
    @staticmethod
    async def update(identifier: int, product: CreateProduct):
        return await prisma_connection.product.update({
            where: {"identifier": identifier},
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
        return await prisma_connection.product.delete(identifier)
