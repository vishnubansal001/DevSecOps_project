from fastapi import APIRouter, Path, HTTPException
from schema import ResponseSchema
from Service.Operator import OperatorService
from Model.operator import CreateOperator,RetrieveOperator
from fastapi.responses import Response
from Repository.Operator import OperatorRepository

router = APIRouter(
    prefix="/operator",
    tags=["operator"],
)

@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_operator():
    try:
        Operator_service = OperatorService()
        result = await Operator_service.get_operators()
        return ResponseSchema(detail="Successfully get all operator", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.head("/{identifier}", tags=["operator"], description="Provide headers that would be returned for a GET request")
async def head_product(identifier: int):
    try:
        result = await OperatorRepository.get_operator(identifier)
        headers = {"Content-Type": "application/json"}
        headers["Content-Length"] = str(len(result.json()))
        response = Response(content=None, headers=headers, media_type="application/json")
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{operator_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_operator_by_id(operator_id: int = Path(..., alias="operator_id")):
    try:
        Operator_service = OperatorService()
        result = await Operator_service.get_operator(operator_id)
        return ResponseSchema(detail="Successfully get operator by id", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_operator(operator: CreateOperator):
    try:
        Operator_service = OperatorService()
        result = await Operator_service.create(operator)
        return ResponseSchema(detail="Successfully create operator", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_operator(operator: RetrieveOperator):
    try:
        Operator_service = OperatorService()
        result = await Operator_service.update(operator)
        return ResponseSchema(detail="Successfully update operator")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{operator_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_operator(operator_id: int = Path(..., alias="operator_id")):
    try:
        Operator_service = OperatorService()
        result = await Operator_service.delete(operator_id)
        return ResponseSchema(detail="Successfully delete operator")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))