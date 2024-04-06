from Repository.ProductComponent import ProductComponentRepository
from Model.productComponent import CreateProductComponent,RetrieveProductComponent

class ProductComponentService:

    @staticmethod
    async def get_productComponents():
        return await ProductComponentRepository.get_productComponents()

    @staticmethod
    async def get_productComponent(identifier: int):
        return await ProductComponentRepository.get_productComponent(identifier)

    @staticmethod
    async def create(productComponent: CreateProductComponent):
        return await ProductComponentRepository.create(productComponent)

    @staticmethod
    async def update(productComponent: RetrieveProductComponent):
        return await ProductComponentRepository.update(productComponent)
    
    @staticmethod
    async def delete(identifier: int):
        return await ProductComponentRepository.delete(identifier)