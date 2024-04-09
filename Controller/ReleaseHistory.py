from fastapi import APIRouter, Path, HTTPException
from schema import ResponseSchema
from Service.ReleaseHistory import ReleaseHistoryService
from Model.releaseHistory import CreateReleaseHistory,RetrieveReleaseHistory

router = APIRouter(
    prefix="/releasehistory",
    tags=["releasehistory"],
)

@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_releaseHistory():
    try:
        result = await ReleaseHistoryService.get_releaseHistorys()
        return ResponseSchema(detail="Successfully get all releasehistory", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{releasehistory_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_releaseHistory_by_id(releasehistory_id: int = Path(..., alias="releasehistory_id")):
    try:
        result = await ReleaseHistoryService.get_releaseHistory(releasehistory_id)
        return ResponseSchema(detail="Successfully get releasehistory by id", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_releaseHistory(releasehistory: CreateReleaseHistory):
    try:
        result = await ReleaseHistoryService.create(releasehistory)
        return ResponseSchema(detail="Successfully create releasehistory", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_releaseHistory(releasehistory: RetrieveReleaseHistory):
    try:
        await ReleaseHistoryService.update(releasehistory)
        return ResponseSchema(detail="Successfully update releasehistory")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{releasehistory_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_releaseHistory(releasehistory_id: int = Path(..., alias="releasehistory_id")):
    try:
        await ReleaseHistoryService.delete(releasehistory_id)
        return ResponseSchema(detail="Successfully delete releasehistory")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))