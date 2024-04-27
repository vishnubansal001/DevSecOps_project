from Repository.Database import Database
from Model.product import CreateProduct, RetrieveProduct
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
        result = self.get_one("product", identifier)
        if result is None:
            raise HTTPException(status_code=402, detail="Item not found")
        return result

    async def create(self, product: CreateProduct):
        if product is None:
            raise HTTPException(status_code=400, detail="No item Provided")
        a = await prisma_connection.prisma.configuration.find_first(where={"identifier": product.configuration})
        if a is None:
            raise HTTPException(status_code=402, detail="No Configuration Found")
        return await self.add_item("product", product.dict())
    
    async def update(self, product: RetrieveProduct):
        if product is None:
            raise HTTPException(status_code=400, detail="No item Provided")
        temp = await prisma_connection.prisma.product.find_first(where={"identifier": product.identifier})
        if temp is None:
            raise HTTPException(status_code=402, detail="Product not found")
        a = await prisma_connection.prisma.configuration.find_first(where={"identifier": product.configuration})
        if a is None:
            raise HTTPException(status_code=402, detail="Configuration not found")
        return await self.update_one("product", product.identifier, product.dict())
    
    async def delete(self, identifier: int):
        if identifier is None:
            raise HTTPException(status_code=400, detail="No identifier Provided")
        temp = await prisma_connection.prisma.product.find_first(where={"identifier": identifier})
        if temp is None:
            raise HTTPException(status_code=402, detail="Product not found")
        return await self.delete_one("product", identifier)

    async def head_get_one(self, identifier: int):
        return await self.head_get_one("product", identifier)
