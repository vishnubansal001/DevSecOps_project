from Repository.Component import ComponentRepository
from Model.component import CreateComponent,RetrieveComponent

class ComponentService:

    @staticmethod
    async def get_components():
        return await ComponentRepository.get_components()

    @staticmethod
    async def get_component(identifier: int):
        return await ComponentRepository.get_component(identifier)

    @staticmethod
    async def create(component: CreateComponent):
        return await ComponentRepository.create(component)

    @staticmethod
    async def update(component: RetrieveComponent):
        return await ComponentRepository.update(component)
    
    @staticmethod
    async def delete(identifier: int):
        return await ComponentRepository.delete(identifier)