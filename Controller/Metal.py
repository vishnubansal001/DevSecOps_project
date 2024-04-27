from fastapi import APIRouter, Path, HTTPException
from schema import ResponseSchema
from Service.Metal import MetalService
from Model.metal import CreateMetal,RetrieveMetal
from fastapi.responses import Response
from Repository.Metal import MetalRepository

router = APIRouter(
    prefix="/metal",
    tags=["metal"],
)

@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_metal():
    try:
        Metal_service = MetalService()
        result = await Metal_service.get_metals()
        return ResponseSchema(detail="Successfully get all metal", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.head("/{identifier}", tags=["metal"], description="Provide headers that would be returned for a GET request")
async def head_product(identifier: int):
    try:
        result = await MetalRepository.get_metal(identifier)
        headers = {"Content-Type": "application/json"}
        headers["Content-Length"] = str(len(result.json()))
        response = Response(content=None, headers=headers, media_type="application/json")
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{metal_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_metal_by_id(metal_id: int = Path(..., alias="metal_id")):
    try:
        Metal_service = MetalService()
        result = await Metal_service.get_metal(metal_id)
        return ResponseSchema(detail="Successfully get metal by id", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_metal(metal: CreateMetal):
    try:
        Metal_service = MetalService()
        result = await Metal_service.create(metal)
        return ResponseSchema(detail="Successfully create metal", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_metal(metal: RetrieveMetal):
    try:
        Metal_service = MetalService()
        result = await Metal_service.update(metal)
        return ResponseSchema(detail="Successfully update metal")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/{metal_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_metal(metal_id: int = Path(..., alias="metal_id")):
    try:
        Metal_service = MetalService()
        result = await Metal_service.delete(metal_id)
        return ResponseSchema(detail="Successfully delete metal")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))