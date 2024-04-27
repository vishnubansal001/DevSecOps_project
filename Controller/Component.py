from fastapi import APIRouter, Path, HTTPException
from schema import ResponseSchema
from Service.Component import ComponentService
from Model.component import CreateComponent,RetrieveComponent
from fastapi.responses import Response
from Repository.Component import ComponentRepository

router = APIRouter(
    prefix="/component",
    tags=["component"],
)

@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_component():
    try:
        component_service = ComponentService()
        result = await component_service.get_components()
        return ResponseSchema(detail="Successfully get all component", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.head("/{identifier}", tags=["component"], description="Provide headers that would be returned for a GET request")
async def head_product(identifier: int):
    try:
        result = await ComponentRepository.get_component(identifier)
        # print(result.json())
        headers = {"Content-Type": "application/json"}
        headers["Content-Length"] = str(len(result.json()))
        response = Response(content=None, headers=headers, media_type="application/json")
        return response
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{component_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_component_by_id(component_id: int = Path(..., alias="component_id")):
    try:
        component_service = ComponentService()
        result = await component_service.get_component(component_id)
        return ResponseSchema(detail="Successfully get component by id", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_component(component: CreateComponent):
    try:
        component_service = ComponentService()
        result = await component_service.create(component)
        return ResponseSchema(detail="Successfully create component", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_component(component: RetrieveComponent):
    try:
        component_service = ComponentService()
        result = await component_service.update(component)
        return ResponseSchema(detail="Successfully update component")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{component_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_component(component_id: int = Path(..., alias="component_id")):
    try:
        component_service = ComponentService()
        result = await component_service.delete(component_id)
        return ResponseSchema(detail="Successfully delete component")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))