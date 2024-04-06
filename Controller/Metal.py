from fastapi import APIRouter, Path, HTTPException
from schema import ResponseSchema
from Service.Metal import MetalService
from Model.metal import CreateMetal,RetrieveMetal

router = APIRouter(
    prefix="/metal",
    tags=["metal"],
)

@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_metal():
    try:
        result = await MetalService.get_metals()
        return ResponseSchema(detail="Successfully get all metal", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{metal_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_metal_by_id(metal_id: int = Path(..., alias="metal_id")):
    try:
        result = await MetalService.get_metal(metal_id)
        return ResponseSchema(detail="Successfully get metal by id", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_metal(metal: CreateMetal):
    try:
        result = await MetalService.create(metal)
        return ResponseSchema(detail="Successfully create metal", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_metal(metal: RetrieveMetal):
    try:
        await MetalService.update(metal)
        return ResponseSchema(detail="Successfully update metal")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/{metal_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_metal(metal_id: int = Path(..., alias="metal_id")):
    try:
        await MetalService.delete(metal_id)
        return ResponseSchema(detail="Successfully delete metal")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))