from fastapi import APIRouter, Path, HTTPException
from schema import ResponseSchema
from Service.MetalEnvironment import MetalEnvironmentService
from Model.metalEnvironment import CreateMetalEnvironment,RetrieveMetalEnvironment

router = APIRouter(
    prefix="/metalenvironment",
    tags=["metalenvironment"],
)

@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_metalEnvironment():
    try:
        result = await MetalEnvironmentService.get_metalEnvironments()
        return ResponseSchema(detail="Successfully get all metalenvironment", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{metalenvironment_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_metalEnvironment_by_id(metalenvironment_id: int = Path(..., alias="metalenvironment_id")):
    try:
        result = await MetalEnvironmentService.get_metalEnvironment(metalenvironment_id)
        return ResponseSchema(detail="Successfully get metalenvironment by id", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_metalEnvironment(metalenvironment: CreateMetalEnvironment):
    try:
        result = await MetalEnvironmentService.create(metalenvironment)
        return ResponseSchema(detail="Successfully create metalenvironment", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_metalEnvironment(metalenvironment: RetrieveMetalEnvironment):
    try:
        await MetalEnvironmentService.update(metalenvironment)
        return ResponseSchema(detail="Successfully update metalenvironment")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{metalenvironment_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_metalEnvironment(metalenvironment_id: int = Path(..., alias="metalenvironment_id")):
    try:
        await MetalEnvironmentService.delete(metalenvironment_id)
        return ResponseSchema(detail="Successfully delete metalenvironment")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))