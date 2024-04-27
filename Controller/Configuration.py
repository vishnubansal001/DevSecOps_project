from fastapi import APIRouter, Path, HTTPException
from schema import ResponseSchema
from Service.Configuration import ConfigurationService
from Model.configuration import CreateConfiguration,RetrieveConfiguration
from fastapi.responses import Response
from Repository.Configuration import ConfigurationRepository

router = APIRouter(
    prefix="/configuration",
    tags=["configuration"],
)

@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_configuration():
    try:
        Configuration_service = ConfigurationService()
        result = await Configuration_service.get_configurations()
        return ResponseSchema(detail="Successfully get all configuration", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.head("/{identifier}", tags=["configuration"], description="Provide headers that would be returned for a GET request")
async def head_product(identifier: int):
    try:
        result = await ConfigurationRepository.get_configuration(identifier)
        print(result.json())
        headers = {"Content-Type": "application/json"}
        headers["Content-Length"] = str(len(result.json()))
        response = Response(content=None, headers=headers, media_type="application/json")
        return response
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{configuration_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_configuration_by_id(configuration_id: int = Path(..., alias="configuration_id")):
    try:
        Configuration_service = ConfigurationService()
        result = await Configuration_service.get_configuration(configuration_id)
        return ResponseSchema(detail="Successfully get configuration by id", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_configuration(configuration: CreateConfiguration):
    try:
        Configuration_service = ConfigurationService()
        result = await Configuration_service.create(configuration)
        return ResponseSchema(detail="Successfully create configuration", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_configuration(configuration: RetrieveConfiguration):
    try:
        Configuration_service = ConfigurationService()
        result = await Configuration_service.update(configuration)
        return ResponseSchema(detail="Successfully update configuration")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{configuration_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_configuration(configuration_id: int = Path(..., alias="configuration_id")):
    try:
        Configuration_service = ConfigurationService()
        result = await Configuration_service.delete(configuration_id)
        return ResponseSchema(detail="Successfully delete configuration")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))