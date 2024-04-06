from Model.request import CreateRequest,RetrieveRequest
from Config.Connection import prisma_connection
from fastapi import HTTPException

class RequestRepository:

    @staticmethod
    async def get_requests():
        return await prisma_connection.prisma.request.find_many()

    @staticmethod
    async def get_request(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        result = await prisma_connection.prisma.request.find_first(where={"identifier": identifier})
        if result is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return result
    
    @staticmethod
    async def create(request: CreateRequest):
        if request is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.release.find_first(where={"identifier": request.release})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.request.create({
            "release": request.release,
            "created": request.created,
            "status": request.status,
            "documentation": request.documentation
        })
    
    @staticmethod
    async def update(request: RetrieveRequest):
        if request is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.request.find_first(where={"identifier": request.identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        a = await prisma_connection.prisma.release.find_first(where={"identifier": request.release})
        if a is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.request.update({
            where: {"identifier": request.identifier},
            data: {
                "release": request.release,
                "created": request.created,
                "status": request.status,
                "documentation": request.documentation
            }
        })
    
    @staticmethod
    async def delete(identifier: int):
        if identifier is None:
            raise HTTPException(status_code=404, detail="Item not found")
        temp = await prisma_connection.prisma.request.find_first(where={"identifier": identifier})
        if temp is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return await prisma_connection.prisma.request.delete(where={"identifier": identifier})