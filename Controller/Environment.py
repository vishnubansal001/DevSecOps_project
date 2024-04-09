from fastapi import APIRouter, Path, HTTPException
from schema import ResponseSchema
from Service.Environment import EnvironmentService
from Model.environment import CreateEnvironment,RetrieveEnvironment

router = APIRouter(
    prefix="/environment",
    tags=["environment"],
)

@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_environment():
    try:
        result = await EnvironmentService.get_environments()
        return ResponseSchema(detail="Successfully get all environment", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{environment_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_environment_by_id(environment_id: int = Path(..., alias="environment_id")):
    try:
        result = await EnvironmentService.get_environment(environment_id)
        return ResponseSchema(detail="Successfully get environment by id", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_environment(environment: CreateEnvironment):
    try:
        result = await EnvironmentService.create(environment)
        return ResponseSchema(detail="Successfully create environment", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_environment(environment: RetrieveEnvironment):
    try:
        await EnvironmentService.update(environment)
        return ResponseSchema(detail="Successfully update environment")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{environment_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_environment(environment_id: int = Path(..., alias="environment_id")):
    try:
        await EnvironmentService.delete(environment_id)
        return ResponseSchema(detail="Successfully delete environment")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))