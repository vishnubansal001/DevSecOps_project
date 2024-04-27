from Model.product import CreateProduct, RetrieveProduct
from Repository.Database import Database
from fastapi import HTTPException
from Config.Connection import prisma_connection

class ProductService(Database):
    def __init__(self):
        super().__init__()

    async def get_products(self):
        return await self.get_all("product")
    
    async def get_product(self, identifier: int):
        if identifier is None:
            raise HTTPException(status_code=400, detail="Item not found")
        result = await self.get_one("product", identifier)
        if result is None:
            raise HTTPException(status_code=402, detail="Item not found")
        return result

    async def create(self, product: CreateProduct):
        if product is None:
            raise HTTPException(status_code=400, detail="No item Provided")
        a = await self.get_one("configuration", product.configuration)
        if a is None:
            raise HTTPException(status_code=402, detail="No Configuration Found")
        return await self.add_item("product", product.dict())
    
    async def update(self, product: RetrieveProduct):
        if product is None:
            raise HTTPException(status_code=400, detail="No item Provided")
        temp = await self.get_one("product", product.identifier)
        if temp is None:
            raise HTTPException(status_code=402, detail="Product not found")
        a = await self.get_one("configuration", product.configuration)
        if a is None:
            raise HTTPException(status_code=402, detail="Configuration not found")
        return await self.update_one("product", product.identifier, product.dict())
    
    async def delete(self, identifier: int):
        if identifier is None:
            raise HTTPException(status_code=400, detail="No identifier Provided")
        temp = await self.get_one("product", identifier)
        if temp is None:
            raise HTTPException(status_code=402, detail="Product not found")
        return await self.delete_one("product", identifier)