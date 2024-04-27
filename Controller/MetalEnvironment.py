from fastapi import APIRouter, Path, HTTPException
from schema import ResponseSchema
from Service.MetalEnvironment import MetalEnvironmentService
from Model.metalEnvironment import CreateMetalEnvironment,RetrieveMetalEnvironment
from fastapi.responses import Response
from Repository.MetalEnvironment import MetalEnvironmentRepository

router = APIRouter(
    prefix="/metalenvironment",
    tags=["metalenvironment"],
)

@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_metalEnvironment():
    try:
        MetalEnvironment_service = MetalEnvironmentService()
        result = await MetalEnvironment_service.get_metalEnvironments()
        return ResponseSchema(detail="Successfully get all metalenvironment", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.head("/{identifier}", tags=["metalenvironment"], description="Provide headers that would be returned for a GET request")
async def head_product(identifier: int):
    try:
        result = await MetalEnvironmentRepository.get_metalEnvironment(identifier)
        headers = {"Content-Type": "application/json"}
        headers["Content-Length"] = str(len(result.json()))
        response = Response(content=None, headers=headers, media_type="application/json")
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{metalenvironment_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_metalEnvironment_by_id(metalenvironment_id: int = Path(..., alias="metalenvironment_id")):
    try:
        MetalEnvironment_service = MetalEnvironmentService()
        result = await MetalEnvironment_service.get_metalEnvironment(metalenvironment_id)
        return ResponseSchema(detail="Successfully get metalenvironment by id", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_metalEnvironment(metalenvironment: CreateMetalEnvironment):
    try:
        MetalEnvironment_service = MetalEnvironmentService()
        result = await MetalEnvironment_service.create(metalenvironment)
        return ResponseSchema(detail="Successfully create metalenvironment", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_metalEnvironment(metalenvironment: RetrieveMetalEnvironment):
    try:
        MetalEnvironment_service = MetalEnvironmentService()
        result = await MetalEnvironment_service.update(metalenvironment)
        return ResponseSchema(detail="Successfully update metalenvironment")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{metalenvironment_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_metalEnvironment(metalenvironment_id: int = Path(..., alias="metalenvironment_id")):
    try:
        MetalEnvironment_service = MetalEnvironmentService()
        result = await MetalEnvironment_service.delete(metalenvironment_id)
        return ResponseSchema(detail="Successfully delete metalenvironment")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))