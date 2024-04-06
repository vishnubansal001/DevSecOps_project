from fastapi import APIRouter, Path, HTTPException
from schema import ResponseSchema
from Service.Role import RoleService
from Model.role import CreateRole,RetrieveRole

router = APIRouter(
    prefix="/role",
    tags=["role"],
)

@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_role():
    try:
        result = await RoleService.get_roles()
        return ResponseSchema(detail="Successfully get all role", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{role_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_role_by_id(role_id: int = Path(..., alias="role_id")):
    try:
        result = await RoleService.get_role(role_id)
        return ResponseSchema(detail="Successfully get role by id", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_role(role: CreateRole):
    try:
        result = await RoleService.create(role)
        return ResponseSchema(detail="Successfully create role", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_role(role: RetrieveRole):
    try:
        await RoleService.update(role)
        return ResponseSchema(detail="Successfully update role")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{role_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_role(role_id: int = Path(..., alias="role_id")):
    try:
        await RoleService.delete(role_id)
        return ResponseSchema(detail="Successfully delete role")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))