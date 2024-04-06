from fastapi import APIRouter, Path, HTTPException
from schema import ResponseSchema
from Service.Release import ReleaseService
from Model.release import CreateRelease,RetrieveRelease

router = APIRouter(
    prefix="/release",
    tags=["release"],
)

@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_release():
    try:
        result = await ReleaseService.get_releases()
        return ResponseSchema(detail="Successfully get all release", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{release_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_release_by_id(release_id: int = Path(..., alias="release_id")):
    try:
        result = await ReleaseService.get_release(release_id)
        return ResponseSchema(detail="Successfully get release by id", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_release(release: CreateRelease):
    try:
        result = await ReleaseService.create(release)
        return ResponseSchema(detail="Successfully create release", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_release(release: RetrieveRelease):
    try:
        await ReleaseService.update(release)
        return ResponseSchema(detail="Successfully update release")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{release_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_release(release_id: int = Path(..., alias="release_id")):
    try:
        await ReleaseService.delete(release_id)
        return ResponseSchema(detail="Successfully delete release")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))