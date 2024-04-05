from fastapi import APIRouter, Path, HTTPException
from schema import ResponseSchema
from Service.Configuration import ConfigurationService
from Model.configuration import CreateConfiguration,RetrieveConfiguration

router = APIRouter(
    prefix="/configuration",
    tags=["configuration"],
)

@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_configuration():
    try:
        result = await ConfigurationService.get_configurations()
        return ResponseSchema(detail="Successfully get all configuration", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{configuration_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_configuration_by_id(configuration_id: int = Path(..., alias="configuration_id")):
    try:
        result = await ConfigurationService.get_configuration(configuration_id)
        return ResponseSchema(detail="Successfully get configuration by id", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_configuration(configuration: CreateConfiguration):
    try:
        result = await ConfigurationService.create(configuration)
        return ResponseSchema(detail="Successfully create configuration", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_configuration(configuration: RetrieveConfiguration):
    try:
        await ConfigurationService.update(configuration)
        return ResponseSchema(detail="Successfully update configuration")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{configuration_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_configuration(configuration_id: int = Path(..., alias="configuration_id")):
    try:
        await ConfigurationService.delete(configuration_id)
        return ResponseSchema(detail="Successfully delete configuration")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))