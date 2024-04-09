from Repository.Configuration import ConfigurationRepository
from Model.configuration import CreateConfiguration,RetrieveConfiguration

class ConfigurationService:

    @staticmethod
    async def get_configurations():
        return await ConfigurationRepository.get_configurations()

    @staticmethod
    async def get_configuration(identifier: int):
        return await ConfigurationRepository.get_configuration(identifier)

    @staticmethod
    async def create(configuration: CreateConfiguration):
        return await ConfigurationRepository.create(configuration)

    @staticmethod
    async def update(configuration: RetrieveConfiguration):
        return await ConfigurationRepository.update(configuration)
    
    @staticmethod
    async def delete(identifier: int):
        return await ConfigurationRepository.delete(identifier)