from fastapi import APIRouter, Path, HTTPException
from schema import ResponseSchema
from Service.ProductHistory import ProductHistoryService
from Model.productHistory import CreateProductHistory,RetrieveProductHistory

router = APIRouter(
    prefix="/producthistory",
    tags=["producthistory"],
)

@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_productHistory():
    try:
        ProductHistory_service = ProductHistoryService()
        result = await ProductHistory_service.get_productHistorys()
        return ResponseSchema(detail="Successfully get all producthistory", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{producthistory_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_productHistory_by_id(producthistory_id: int = Path(..., alias="producthistory_id")):
    try:
        ProductHistory_service = ProductHistoryService()
        result = await ProductHistory_service.get_productHistory(producthistory_id)
        return ResponseSchema(detail="Successfully get producthistory by id", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_productHistory(producthistory: CreateProductHistory):
    try:
        ProductHistory_service = ProductHistoryService()
        result = await ProductHistory_service.create(producthistory)
        return ResponseSchema(detail="Successfully create producthistory", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_productHistory(producthistory: RetrieveProductHistory):
    try:
        ProductHistory_service = ProductHistoryService()
        result = await ProductHistory_service.update(producthistory)
        return ResponseSchema(detail="Successfully update producthistory")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{producthistory_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_productHistory(producthistory_id: int = Path(..., alias="producthistory_id")):
    try:
        ProductHistory_service = ProductHistoryService()
        result = await ProductHistory_service.delete(producthistory_id)
        return ResponseSchema(detail="Successfully delete producthistory")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))