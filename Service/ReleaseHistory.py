from Repository.ReleaseHistory import ReleaseHistoryRepository
from Model.releaseHistory import CreateReleaseHistory,RetrieveReleaseHistory

class ReleaseHistoryService:

    @staticmethod
    async def get_releaseHistorys():
        return await ReleaseHistoryRepository.get_releaseHistorys()

    @staticmethod
    async def get_releaseHistory(identifier: int):
        return await ReleaseHistoryRepository.get_releaseHistory(identifier)

    @staticmethod
    async def create(releaseHistory: CreateReleaseHistory):
        return await ReleaseHistoryRepository.create(releaseHistory)

    @staticmethod
    async def update(releaseHistory: RetrieveReleaseHistory):
        return await ReleaseHistoryRepository.update(releaseHistory)
    
    @staticmethod
    async def delete(identifier: int):
        return await ReleaseHistoryRepository.delete(identifier)