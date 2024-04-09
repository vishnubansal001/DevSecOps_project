from Repository.Environment import EnvironmentRepository
from Model.environment import CreateEnvironment,RetrieveEnvironment

class EnvironmentService:

    @staticmethod
    async def get_environments():
        return await EnvironmentRepository.get_environments()

    @staticmethod
    async def get_environment(identifier: int):
        return await EnvironmentRepository.get_environment(identifier)

    @staticmethod
    async def create(environment: CreateEnvironment):
        return await EnvironmentRepository.create(environment)

    @staticmethod
    async def update(environment: RetrieveEnvironment):
        return await EnvironmentRepository.update(environment)
    
    @staticmethod
    async def delete(identifier: int):
        return await EnvironmentRepository.delete(identifier)