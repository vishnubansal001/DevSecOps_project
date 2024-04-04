from Model.product import CreateProduct,RetrieveProduct
from Config.Connection import prisma_connection

class ProductRepository:

    @staticmethod
    async def get_products():
        return await prisma_connection.prisma.product.find_many()
    
    @staticmethod
    async def get_product(identifier: int):
        return await prisma_connection.prisma.product.find_first(where={"identifier": identifier})

    @staticmethod
    async def create(product: CreateProduct):
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
        return await prisma_connection.prisma.product.delete(identifier)
