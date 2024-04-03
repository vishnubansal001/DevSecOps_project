from fastapi import APIRouter, Path
from schema import ResponseSchema
from Service.Product import ProductService
from Model.product import CreateProduct

router = APIRouter(
    prefix="/product",
    tags=["product"],
)

@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_product():
    result = await ProductService.get_products()
    return ResponseSchema(detail="Successfully get all product", result=result)

@router.get("/{product_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_product_by_id(product_id: int = Path(..., alias="product_id")):
    result = await ProductService.get_product(product_id)
    return ResponseSchema(detail="Successfully get product by id", result=result)

@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_product(product: CreateProduct):
    result = await ProductService.create(product)
    return ResponseSchema(detail="Successfully create product", result=result)

@router.put("/{product_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_product(product_id: int = Path(..., alias="product_id"),*, product: CreateProduct):
    await ProductService.update(product_id, product)
    return ResponseSchema(detail="Successfully update product", result=result)

@router.delete("/{product_id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def delete_product(product_id: int = Path(..., alias="product_id")):
    await ProductService.delete(product_id)
    return ResponseSchema(detail="Successfully delete product")