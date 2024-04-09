from Repository.ComponentHistory import ComponentHistoryRepository
from Model.componentHistory import CreateComponentHistory,RetrieveComponentHistory

class ComponentHistoryService:

    @staticmethod
    async def get_componentHistorys():
        return await ComponentHistoryRepository.get_componentHistorys()

    @staticmethod
    async def get_componentHistory(identifier: int):
        return await ComponentHistoryRepository.get_componentHistory(identifier)

    @staticmethod
    async def create(componentHistory: CreateComponentHistory):
        return await ComponentHistoryRepository.create(componentHistory)

    @staticmethod
    async def update(componentHistory: RetrieveComponentHistory):
        return await ComponentHistoryRepository.update(componentHistory)
    
    @staticmethod
    async def delete(identifier: int):
        return await ComponentHistoryRepository.delete(identifier)