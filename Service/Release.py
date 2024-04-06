from Repository.Release import ReleaseRepository
from Model.release import CreateRelease,RetrieveRelease

class ReleaseService:

    @staticmethod
    async def get_releases():
        return await ReleaseRepository.get_releases()

    @staticmethod
    async def get_release(identifier: int):
        return await ReleaseRepository.get_release(identifier)

    @staticmethod
    async def create(release: CreateRelease):
        return await ReleaseRepository.create(release)

    @staticmethod
    async def update(release: RetrieveRelease):
        return await ReleaseRepository.update(release)
    
    @staticmethod
    async def delete(identifier: int):
        return await ReleaseRepository.delete(identifier)