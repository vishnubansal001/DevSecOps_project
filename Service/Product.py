from Repository.Database import Database
from Model.product import CreateProduct, RetrieveProduct
from fastapi import HTTPException

class ProductService(Database):
    def __init__(self):
        super().__init__()

    async def get_products(self):
        return await self.get_all("product")
    
    async def get_product(self, identifier: int):
        if identifier is None:
            raise HTTPException(status_code=400, detail="Item not found")
        result = self.get_one("product", identifier)
        if result is None:
            raise HTTPException(status_code=402, detail="Item not found")
        return result

    async def create(self, product: CreateProduct):
        return await self.add_item("product", product.dict())
    
    async def update(self, product: RetrieveProduct):
        return await self.update_one("product", product.identifier, product.dict())
    
    async def delete(self, identifier: int):
        return await self.delete_one("product", identifier)

    async def head_get_one(self, identifier: int):
        return await self.head_get_one("product", identifier)
