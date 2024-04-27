from Model.productHistory import CreateProductHistory,RetrieveProductHistory
from Repository.Database import Database
from fastapi import HTTPException

class ProductHistoryService(Database):
    def __init__(self):
        super().__init__()

    async def get_product_histories(self):
        return await self.get_all("productHistory")

    async def get_product_history(self, identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await self.get_one("productHistory", identifier)
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result
    
    async def create(self, productHistory: CreateProductHistory):
        if productHistory is None:
            raise HTTPException(status_code=404, detail="Item not found")
        a = await self.get_one("product", productHistory.product)
        if a is None:
            raise HTTPException(status_code=404, detail="Item not found")
        b = await self.get_one("operator", productHistory.operator)
        if b is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.add_item("productHistory", productHistory.dict())
    
    async def update(self, productHistory: RetrieveProductHistory):
        if productHistory is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("productHistory", productHistory.identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        a = await self.get_one("product", productHistory.product)
        if a is None:
            raise HTTPException(status_code=404, detail="Item not found")
        b = await self.get_one("operator", productHistory.operator)
        if b is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.update_one("productHistory", productHistory.identifier, productHistory.dict())
    
    async def delete(self, identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("productHistory", identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.delete_one("productHistory", identifier)