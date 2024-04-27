from fastapi import APIRouter, Path, HTTPException
from schema import ResponseSchema
from Service.Environment import EnvironmentService
from Model.environment import CreateEnvironment,RetrieveEnvironment
from fastapi.responses import Response
from Repository.Environment import EnvironmentRepository

router = APIRouter(
    prefix="/environment",
    tags=["environment"],
)

@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_environment():
    try:
        Environment_service = EnvironmentService()
        result = await Environment_service.get_environments()
        return ResponseSchema(detail="Successfully get all environment", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.head("/{identifier}", tags=["environment"], description="Provide headers that would be returned for a GET request")
async def head_product(identifier: int):
    try:
        result = await EnvironmentRepository.get_environment(identifier)
        print(result.json())
        headers = {"Content-Type": "application/json"}
        headers["Content-Length"] = str(len(result.json()))
        response = Response(content=None, headers=headers, media_type="application/json")
        return response
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{environment_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_environment_by_id(environment_id: int = Path(..., alias="environment_id")):
    try:
        Environment_service = EnvironmentService()
        result = await Environment_service.get_environment(environment_id)
        return ResponseSchema(detail="Successfully get environment by id", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_environment(environment: CreateEnvironment):
    try:
        Environment_service = EnvironmentService()
        result = await Environment_service.create(environment)
        return ResponseSchema(detail="Successfully create environment", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_environment(environment: RetrieveEnvironment):
    try:
        Environment_service = EnvironmentService()
        result = await Environment_service.update(environment)
        return ResponseSchema(detail="Successfully update environment")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{environment_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_environment(environment_id: int = Path(..., alias="environment_id")):
    try:
        Environment_service = EnvironmentService()
        result = await Environment_service.delete(environment_id)
        return ResponseSchema(detail="Successfully delete environment")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))