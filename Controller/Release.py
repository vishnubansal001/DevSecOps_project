from fastapi import APIRouter, Path, HTTPException
from schema import ResponseSchema
from Service.Release import ReleaseService
from Model.release import CreateRelease,RetrieveRelease
from fastapi.responses import Response
from Repository.Release import ReleaseRepository


router = APIRouter(
    prefix="/release",
    tags=["release"],
)

@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_release():
    try:
        Release_service = ReleaseService()
        result = await Release_service.get_releases()
        return ResponseSchema(detail="Successfully get all release", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.head("/{identifier}", tags=["release"], description="Provide headers that would be returned for a GET request")
async def head_product(identifier: int):
    try:
        result = await ReleaseRepository.get_release(identifier)
        headers = {"Content-Type": "application/json"}
        headers["Content-Length"] = str(len(result.json()))
        response = Response(content=None, headers=headers, media_type="application/json")
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{release_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_release_by_id(release_id: int = Path(..., alias="release_id")):
    try:
        Release_service = ReleaseService()
        result = await Release_service.get_release(release_id)
        return ResponseSchema(detail="Successfully get release by id", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_release(release: CreateRelease):
    try:
        Release_service = ReleaseService()
        result = await Release_service.create(release)
        return ResponseSchema(detail="Successfully create release", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_release(release: RetrieveRelease):
    try:
        Release_service = ReleaseService()
        result = await Release_service.update(release)
        return ResponseSchema(detail="Successfully update release")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{release_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_release(release_id: int = Path(..., alias="release_id")):
    try:
        Release_service = ReleaseService()
        result = await Release_service.delete(release_id)
        return ResponseSchema(detail="Successfully delete release")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))