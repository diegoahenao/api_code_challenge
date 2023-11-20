from fastapi import APIRouter
from database.database import sessionlocal
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from services.queries import Query

queries_router = APIRouter()

@queries_router.get('/query_one', tags=['queries'], response_model=dict, status_code=200)
def query_one_api() -> dict:
    db = sessionlocal()
    result = Query(db).get_query_one()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@queries_router.get('/query_two', tags=['queries'], response_model=dict, status_code=200)
def query_two_api() -> dict:
    db = sessionlocal()
    result = Query(db).get_query_two()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))