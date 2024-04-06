from fastapi import APIRouter, Path, HTTPException
from schema import ResponseSchema
from Service.ProductComponent import ProductComponentService
from Model.productComponent import CreateProductComponent,RetrieveProductComponent

router = APIRouter(
    prefix="/productcomponent",
    tags=["productcomponent"],
)

@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_productComponent():
    try:
        result = await ProductComponentService.get_productComponents()
        return ResponseSchema(detail="Successfully get all productcomponent", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{productcomponent_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_productComponent_by_id(productcomponent_id: int = Path(..., alias="productcomponent_id")):
    try:
        result = await ProductComponentService.get_productComponent(productcomponent_id)
        return ResponseSchema(detail="Successfully get productcomponent by id", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_productComponent(productcomponent: CreateProductComponent):
    try:
        result = await ProductComponentService.create(productcomponent)
        return ResponseSchema(detail="Successfully create productcomponent", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_productComponent(productcomponent: RetrieveProductComponent):
    try:
        await ProductComponentService.update(productcomponent)
        return ResponseSchema(detail="Successfully update productcomponent")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{productcomponent_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_productComponent(productcomponent_id: int = Path(..., alias="productcomponent_id")):
    try:
        await ProductComponentService.delete(productcomponent_id)
        return ResponseSchema(detail="Successfully delete productcomponent")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))