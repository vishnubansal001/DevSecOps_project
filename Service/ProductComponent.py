from Model.productComponent import CreateProductComponent,RetrieveProductComponent
from Repository.Database import Database
from fastapi import HTTPException

class ProductComponentService(Database):
    def __init__(self):
        super().__init__()

    async def get_productComponents(self):
        return await self.get_all("productComponent")

    async def get_productComponent(self, identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await self.get_one("productComponent", identifier)
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result

    async def create(self, productComponent: CreateProductComponent):
        if productComponent is None:
            raise HTTPException(status_code=404, detail="Item not found")
        a = await self.get_one("product", productComponent.product)
        if a is None:
            raise HTTPException(status_code=404, detail="Item not found")
        b = await self.get_one("component", productComponent.component)
        if b is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.add_item("productComponent", productComponent.dict())
    
    async def update(self, productComponent: RetrieveProductComponent):
        if productComponent is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("productComponent", productComponent.identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        a = await self.get_one("product", productComponent.product)
        if a is None:
            raise HTTPException(status_code=404, detail="Item not found")
        b = await self.get_one("component", productComponent.component)
        if b is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.update_one("productComponent", productComponent.identifier, productComponent.dict())
    
    async def delete(self, identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("productComponent", identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.delete_one("productComponent", identifier)