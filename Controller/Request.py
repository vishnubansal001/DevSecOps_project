from fastapi import APIRouter, Path, HTTPException
from schema import ResponseSchema
from Service.Request import RequestService
from Model.request import CreateRequest,RetrieveRequest

router = APIRouter(
    prefix="/request",
    tags=["request"],
)

@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_request():
    try:
        Request_service = RequestService()
        result = await Request_service.get_requests()
        return ResponseSchema(detail="Successfully get all request", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{request_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_request_by_id(request_id: int = Path(..., alias="request_id")):
    try:
        Request_service = RequestService()
        result = await Request_service.get_request(request_id)
        return ResponseSchema(detail="Successfully get request by id", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_request(request: CreateRequest):
    try:
        Request_service = RequestService()
        result = await Request_service.create(request)
        return ResponseSchema(detail="Successfully create request", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_request(request: RetrieveRequest):
    try:
        Request_service = RequestService()
        result = await Request_service.update(request)
        return ResponseSchema(detail="Successfully update request")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{request_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_request(request_id: int = Path(..., alias="request_id")):
    try:
        Request_service = RequestService()
        result = await Request_service.delete(request_id)
        return ResponseSchema(detail="Successfully delete request")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))