from Repository.Role import RoleRepository
from Model.role import CreateRole,RetrieveRole

class RoleService:

    @staticmethod
    async def get_roles():
        return await RoleRepository.get_roles()

    @staticmethod
    async def get_role(identifier: int):
        return await RoleRepository.get_role(identifier)

    @staticmethod
    async def create(role: CreateRole):
        return await RoleRepository.create(role)

    @staticmethod
    async def update(role: RetrieveRole):
        return await RoleRepository.update(role)
    
    @staticmethod
    async def delete(identifier: int):
        return await RoleRepository.delete(identifier)