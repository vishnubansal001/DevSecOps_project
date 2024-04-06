from Repository.Request import RequestRepository
from Model.request import CreateRequest,RetrieveRequest

class RequestService:

    @staticmethod
    async def get_requests():
        return await RequestRepository.get_requests()

    @staticmethod
    async def get_request(identifier: int):
        return await RequestRepository.get_request(identifier)

    @staticmethod
    async def create(request: CreateRequest):
        return await RequestRepository.create(request)

    @staticmethod
    async def update(request: RetrieveRequest):
        return await RequestRepository.update(request)
    
    @staticmethod
    async def delete(identifier: int):
        return await RequestRepository.delete(identifier)