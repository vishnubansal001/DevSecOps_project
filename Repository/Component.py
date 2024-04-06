from Model.component import CreateComponent,RetrieveComponent
from Config.Connection import prisma_connection
from fastapi import HTTPException

class ComponentRepository:

    @staticmethod
    async def get_components():
        return await prisma_connection.prisma.component.find_many()

    @staticmethod
    async def get_component(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await prisma_connection.prisma.component.find_first(where={"identifier": identifier})
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result
    
    @staticmethod
    async def create(component: CreateComponent):
        if component is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.configuration.find_first(where={"identifier": component.configuration})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.component.create({
            "created": component.created,
            "fullName": component.fullName,
            "shortName": component.shortName,
            "version": component.version,
            "configuration": component.configuration,
            "status": component.status
        })
    
    @staticmethod
    async def update(component: RetrieveComponent):
        if component is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.component.find_first(where={"identifier": component.identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        r = await prisma_connection.prisma.configuration.find_first(where={"identifier": component.configuration})
        if r is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.component.update({
            where: {"identifier": component.identifier},
            data: {
                "created": component.created,
                "fullName": component.fullName,
                "shortName": component.shortName,
                "version": component.version,
                "configuration": component.configuration,
                "status": component.status
            }
        })
    
    @staticmethod
    async def delete(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.component.find_first(where={"identifier": identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.component.delete(where={"identifier": identifier})