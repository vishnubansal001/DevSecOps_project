from fastapi import APIRouter, Path, HTTPException
from schema import ResponseSchema
from Service.Product import ProductService
from Model.product import CreateProduct, RetrieveProduct
from fastapi.responses import Response
from Repository.Product import ProductRepository

router = APIRouter(
    prefix="/product",
    tags=["product"],
)

@router.head("/{identifier}", tags=["product"], description="Provide headers that would be returned for a GET request")
async def head_product(identifier: int):
    try:
        result = await ProductRepository.get_product(identifier)
        print(result.json())
        headers = {"Content-Type": "application/json"}
        headers["Content-Length"] = str(len(result.json()))
        response = Response(content=None, headers=headers, media_type="application/json")
        return response
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_product():
    try:
        # Instantiate ProductService
        product_service = ProductService()
        result = await product_service.get_products()  # Call instance method
        return ResponseSchema(detail="Successfully get all product", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{product_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_product_by_id(product_id: int = Path(..., alias="product_id")):
    try:
        # Instantiate ProductService
        product_service = ProductService()
        result = await product_service.get_product(product_id)  # Call instance method
        return ResponseSchema(detail="Successfully get product by id", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_product(product: CreateProduct):
    try:
        # Instantiate ProductService
        product_service = ProductService()
        result = await product_service.create(product)  # Call instance method
        return ResponseSchema(detail="Successfully create product", result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_product(product: RetrieveProduct):
    try:
        # Instantiate ProductService
        product_service = ProductService()
        await product_service.update(product)  # Call instance method
        return ResponseSchema(detail="Successfully update product")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{product_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_product(product_id: int = Path(..., alias="product_id")):
    try:
        # Instantiate ProductService
        product_service = ProductService()
        await product_service.delete(product_id)  # Call instance method
        return ResponseSchema(detail="Successfully delete product")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
