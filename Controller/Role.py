from fastapi import APIRouter, Path, HTTPException
from schema import ResponseSchema
from Service.Role import RoleService
from Model.role import CreateRole,RetrieveRole
from fastapi.responses import Response
from Repository.Role import RoleRepository

router = APIRouter(
    prefix="/role",
    tags=["role"],
)

@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_role():
    try:
        Role_service = RoleService()
        result = await Role_service.get_roles()
        return ResponseSchema(detail="Successfully get all role", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.head("/{identifier}", tags=["role"], description="Provide headers that would be returned for a GET request")
async def head_product(identifier: int):
    try:
        result = await RoleRepository.get_role(identifier)
        headers = {"Content-Type": "application/json"}
        headers["Content-Length"] = str(len(result.json()))
        response = Response(content=None, headers=headers, media_type="application/json")
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{role_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_role_by_id(role_id: int = Path(..., alias="role_id")):
    try:
        Role_service = RoleService()
        result = await Role_service.get_role(role_id)
        return ResponseSchema(detail="Successfully get role by id", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_role(role: CreateRole):
    try:
        Role_service = RoleService()
        result = await Role_service.create(role)
        return ResponseSchema(detail="Successfully create role", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_role(role: RetrieveRole):
    try:
        Role_service = RoleService()
        result = await Role_service.update(role)
        return ResponseSchema(detail="Successfully update role")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{role_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_role(role_id: int = Path(..., alias="role_id")):
    try:
        Role_service = RoleService()
        result = await Role_service.delete(role_id)
        return ResponseSchema(detail="Successfully delete role")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))