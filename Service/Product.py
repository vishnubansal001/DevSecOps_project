from Repository.Product import ProductRepository
from Model.product import CreateProduct,RetrieveProduct

class ProductService:

    @staticmethod
    async def get_products():
        return await ProductRepository.get_products()
    
    @staticmethod
    async def get_product(identifier: int):
        return await ProductRepository.get_product(identifier)

    @staticmethod
    async def create(product: CreateProduct):
        return await ProductRepository.create(product)
    
    @staticmethod
    async def update(product: RetrieveProduct):
        return await ProductRepository.update(product)
    
    @staticmethod
    async def delete(identifier: int):
        return await ProductRepository.delete(identifier)