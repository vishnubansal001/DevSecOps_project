from Model.component import CreateComponent,RetrieveComponent
from Repository.Database import Database
from fastapi import HTTPException

class ComponentService(Database):
    def __init__(self):
        super().__init__()
    
    async def get_components(self):
        return await self.get_all("component")

    async def get_component(self, identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result =await self.get_one("component", identifier)
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result

    async def create(self, component: CreateComponent):
        if component is None:
            raise HTTPException(status_code=404, detail="Item not found")
        a= await self.get_one("configuration", component.configuration)
        if a is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.add_item("component", component.dict())

    async def update(self, component: RetrieveComponent):
        if component is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("component", component.identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        r = await self.get_one("configuration", component.configuration)
        if r is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.update_one("component", component.identifier, component.dict())
    
    async def delete(self, identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await self.get_one("component", identifier)
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.delete_one("component", identifier)