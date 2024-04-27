from Model.component import CreateComponent,RetrieveComponent
from Repository.Database import Database
from fastapi import HTTPException
from Config.Connection import prisma_connection

class ComponentService(Database):
    def __init__(self):
        super().__init__()
    
    async def get_components():
        return await self.get_all("component")

    async def get_component(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = self.get_one("component", identifier)
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result

    async def create(component: CreateComponent):
        if component is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.configuration.find_first(where={"identifier": component.configuration})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.add_item("component", component.dict())

    async def update(component: RetrieveComponent):
        if component is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.component.find_first(where={"identifier": component.identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        r = await prisma_connection.prisma.configuration.find_first(where={"identifier": component.configuration})
        if r is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.update_one("component", component.identifier, component.dict())
    
    async def delete(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.component.find_first(where={"identifier": identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await self.delete_one("component", identifier)