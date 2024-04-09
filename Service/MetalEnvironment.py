from Repository.MetalEnvironment import MetalEnvironmentRepository
from Model.metalEnvironment import CreateMetalEnvironment,RetrieveMetalEnvironment

class MetalEnvironmentService:

    @staticmethod
    async def get_metalEnvironments():
        return await MetalEnvironmentRepository.get_metalEnvironments()

    @staticmethod
    async def get_metalEnvironment(identifier: int):
        return await MetalEnvironmentRepository.get_metalEnvironment(identifier)

    @staticmethod
    async def create(metalEnvironment: CreateMetalEnvironment):
        return await MetalEnvironmentRepository.create(metalEnvironment)

    @staticmethod
    async def update(metalEnvironment: RetrieveMetalEnvironment):
        return await MetalEnvironmentRepository.update(metalEnvironment)
    
    @staticmethod
    async def delete(identifier: int):
        return await MetalEnvironmentRepository.delete(identifier)