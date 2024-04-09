from fastapi import APIRouter, Path, HTTPException
from schema import ResponseSchema
from Service.OperatorRole import OperatorRoleService
from Model.operatorRole import CreateOperatorRole,RetrieveOperatorRole

router = APIRouter(
    prefix="/operatorrole",
    tags=["operatorrole"],
)

@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_operatorRole():
    try:
        result = await OperatorRoleService.get_operatorRoles()
        return ResponseSchema(detail="Successfully get all operatorRole", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{operatorRole_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_operatorRole_by_id(operatorRole_id: int = Path(..., alias="operatorRole_id")):
    try:
        result = await OperatorRoleService.get_operatorRole(operatorRole_id)
        return ResponseSchema(detail="Successfully get operatorRole by id", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_operatorRole(operatorRole: CreateOperatorRole):
    try:
        result = await OperatorRoleService.create(operatorRole)
        return ResponseSchema(detail="Successfully create operatorRole", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_operatorRole(operatorRole: RetrieveOperatorRole):
    try:
        await OperatorRoleService.update(operatorRole)
        return ResponseSchema(detail="Successfully update operatorRole")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{operatorRole_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_operatorRole(operatorRole_id: int = Path(..., alias="operatorRole_id")):
    try:
        await OperatorRoleService.delete(operatorRole_id)
        return ResponseSchema(detail="Successfully delete operatorRole")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))