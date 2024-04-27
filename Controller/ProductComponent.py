from fastapi import APIRouter, Path, HTTPException
from schema import ResponseSchema
from Service.ProductComponent import ProductComponentService
from Model.productComponent import CreateProductComponent,RetrieveProductComponent
from fastapi.responses import Response
from Repository.ProductComponent import ProductComponentRepository

router = APIRouter(
    prefix="/productcomponent",
    tags=["productcomponent"],
)

@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_productComponent():
    try:
        ProductComponent_service = ProductComponentService()
        result = await ProductComponent_service.get_productComponents()
        return ResponseSchema(detail="Successfully get all productcomponent", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.head("/{identifier}", tags=["productcomponent"], description="Provide headers that would be returned for a GET request")
async def head_product(identifier: int):
    try:
        result = await ProductComponentRepository.get_productComponent(identifier)
        headers = {"Content-Type": "application/json"}
        headers["Content-Length"] = str(len(result.json()))
        response = Response(content=None, headers=headers, media_type="application/json")
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{productcomponent_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_productComponent_by_id(productcomponent_id: int = Path(..., alias="productcomponent_id")):
    try:
        ProductComponent_service = ProductComponentService()
        result = await ProductComponent_service.get_productComponent(productcomponent_id)
        return ResponseSchema(detail="Successfully get productcomponent by id", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_productComponent(productcomponent: CreateProductComponent):
    try:
        ProductComponent_service = ProductComponentService()
        result = await ProductComponent_service.create(productcomponent)
        return ResponseSchema(detail="Successfully create productcomponent", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_productComponent(productcomponent: RetrieveProductComponent):
    try:
        ProductComponent_service = ProductComponentService()
        result = await ProductComponent_service.update(productcomponent)
        return ResponseSchema(detail="Successfully update productcomponent")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{productcomponent_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_productComponent(productcomponent_id: int = Path(..., alias="productcomponent_id")):
    try:
        ProductComponent_service = ProductComponentService()
        result = await ProductComponent_service.delete(productcomponent_id)
        return ResponseSchema(detail="Successfully delete productcomponent")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))