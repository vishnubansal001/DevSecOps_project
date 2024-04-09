from fastapi import APIRouter, Path, HTTPException
from schema import ResponseSchema
from Service.Operator import OperatorService
from Model.operator import CreateOperator,RetrieveOperator

router = APIRouter(
    prefix="/operator",
    tags=["operator"],
)

@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_operator():
    try:
        result = await OperatorService.get_operators()
        return ResponseSchema(detail="Successfully get all operator", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{operator_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_operator_by_id(operator_id: int = Path(..., alias="operator_id")):
    try:
        result = await OperatorService.get_operator(operator_id)
        return ResponseSchema(detail="Successfully get operator by id", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_operator(operator: CreateOperator):
    try:
        result = await OperatorService.create(operator)
        return ResponseSchema(detail="Successfully create operator", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_operator(operator: RetrieveOperator):
    try:
        await OperatorService.update(operator)
        return ResponseSchema(detail="Successfully update operator")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{operator_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_operator(operator_id: int = Path(..., alias="operator_id")):
    try:
        await OperatorService.delete(operator_id)
        return ResponseSchema(detail="Successfully delete operator")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))