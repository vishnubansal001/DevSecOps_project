from fastapi import APIRouter, Path, HTTPException
from schema import ResponseSchema
from Service.ComponentHistory import ComponentHistoryService
from Model.componentHistory import CreateComponentHistory,RetrieveComponentHistory

router = APIRouter(
    prefix="/componenthistory",
    tags=["componenthistory"],
)

@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_componentHistory():
    try:
        ComponentHistory_service = ComponentHistoryService()
        result = await ComponentHistory_service.get_componentHistorys()
        return ResponseSchema(detail="Successfully get all componenthistory", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{componenthistory_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_componentHistory_by_id(componenthistory_id: int = Path(..., alias="componenthistory_id")):
    try:
        ComponentHistory_service = ComponentHistoryService()
        result = await ComponentHistory_service.get_componentHistory(componenthistory_id)
        return ResponseSchema(detail="Successfully get componenthistory by id", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_componentHistory(componenthistory: CreateComponentHistory):
    try:
        ComponentHistory_service = ComponentHistoryService()
        result = await ComponentHistory_service.create(componenthistory)
        return ResponseSchema(detail="Successfully create componenthistory", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_componentHistory(componenthistory: RetrieveComponentHistory):
    try:
        ComponentHistory_service = ComponentHistoryService()
        result = await ComponentHistory_service.update(componenthistory)
        return ResponseSchema(detail="Successfully update componenthistory")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{componenthistory_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_componentHistory(componenthistory_id: int = Path(..., alias="componenthistory_id")):
    try:
        ComponentHistory_service = ComponentHistoryService()
        result = await ComponentHistory_service.delete(componenthistory_id)
        return ResponseSchema(detail="Successfully delete componenthistory")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))