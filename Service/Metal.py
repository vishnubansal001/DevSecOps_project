from Repository.Metal import MetalRepository
from Model.metal import CreateMetal,RetrieveMetal

class MetalService:

    @staticmethod
    async def get_metals():
        return await MetalRepository.get_metals()

    @staticmethod
    async def get_metal(identifier: int):
        return await MetalRepository.get_metal(identifier)

    @staticmethod
    async def create(metal: CreateMetal):
        return await MetalRepository.create(metal)

    @staticmethod
    async def update(metal: RetrieveMetal):
        return await MetalRepository.update(metal)
    
    @staticmethod
    async def delete(identifier: int):
        return await MetalRepository.delete(identifier)