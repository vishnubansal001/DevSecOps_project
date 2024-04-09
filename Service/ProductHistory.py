from Repository.ProductHistory import ProductHistoryRepository
from Model.productHistory import CreateProductHistory,RetrieveProductHistory

class ProductHistoryService:

    @staticmethod
    async def get_product_histories():
        return await ProductHistoryRepository.get_product_histories()

    @staticmethod
    async def get_product_history(identifier: int):
        return await ProductHistoryRepository.get_product_history(identifier)
    
    @staticmethod
    async def create(productHistory: CreateProductHistory):
        return await ProductHistoryRepository.create(productHistory)
    
    @staticmethod
    async def update(productHistory: RetrieveProductHistory):
        return await ProductHistoryRepository.update(productHistory)
    
    @staticmethod
    async def delete(identifier: int):
        return await ProductHistoryRepository.delete(identifier)