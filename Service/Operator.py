from Repository.Operator import OperatorRepository
from Model.operator import CreateOperator,RetrieveOperator

class OperatorService:

    @staticmethod
    async def get_operators():
        return await OperatorRepository.get_operators()

    @staticmethod
    async def get_operator(identifier: int):
        return await OperatorRepository.get_operator(identifier)

    @staticmethod
    async def create(operator: CreateOperator):
        return await OperatorRepository.create(operator)

    @staticmethod
    async def update(operator: RetrieveOperator):
        return await OperatorRepository.update(operator)
    
    @staticmethod
    async def delete(identifier: int):
        return await OperatorRepository.delete(identifier)