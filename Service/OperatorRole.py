from Repository.OperatorRole import OperatorRoleRepository
from Model.operatorRole import CreateOperatorRole,RetrieveOperatorRole

class OperatorRoleService:

    @staticmethod
    async def get_operatorRoles():
        return await OperatorRoleRepository.get_operatorRoles()

    @staticmethod
    async def get_operatorRole(identifier: int):
        return await OperatorRoleRepository.get_operatorRole(identifier)

    @staticmethod
    async def create(operatorRole: CreateOperatorRole):
        return await OperatorRoleRepository.create(operatorRole)

    @staticmethod
    async def update(operatorRole: RetrieveOperatorRole):
        return await OperatorRoleRepository.update(operatorRole)
    
    @staticmethod
    async def delete(identifier: int):
        return await OperatorRoleRepository.delete(identifier)