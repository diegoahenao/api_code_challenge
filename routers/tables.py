from fastapi import APIRouter, Depends
from schemas.schemas_tables import DepartmentsCreate, JobsCreate, HiredEmployeesCreate
from database.database import sessionlocal
from services.tables import Tables
from typing import List
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer

tables_router = APIRouter()

@tables_router.post('/departments', tags=['tables'], response_model=dict, status_code=201, dependencies=[Depends(JWTBearer())])
def create_department_api(department: DepartmentsCreate) -> dict:
    db = sessionlocal()
    Tables(db).create_department(department)
    return JSONResponse(status_code=201, content={"message": "Departments registered"})

@tables_router.get('/departments', tags=['tables'], response_model=List[DepartmentsCreate], status_code=200)
def read_departments_api() -> List[DepartmentsCreate]:
    db = sessionlocal()
    result = Tables(db).get_departments()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@tables_router.post('/jobs', tags=['tables'], response_model=dict, status_code=201, dependencies=[Depends(JWTBearer())])
def create_job_api(job: JobsCreate) -> dict:
    db = sessionlocal()
    Tables(db).create_job(job)
    return JSONResponse(status_code=201, content={"message": "Jobs registered"})

@tables_router.get('/jobs', tags=['tables'], response_model=List[JobsCreate], status_code=200)
def read_jobs_api() -> List[JobsCreate]:
    db = sessionlocal()
    result = Tables(db).get_jobs()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@tables_router.post('/hired_employees', tags=['tables'], response_model=dict, status_code=201, dependencies=[Depends(JWTBearer())])
def create_hired_employee_api(hired_employee: HiredEmployeesCreate) -> dict:
    db = sessionlocal()
    Tables(db).create_hired_employee(hired_employee)
    return JSONResponse(status_code=201, content={"message": "Hired employees registered"})

@tables_router.get('/hired_employees', tags=['tables'], response_model=List[HiredEmployeesCreate], status_code=200)
def read_hired_employees_api() -> List[HiredEmployeesCreate]:
    db = sessionlocal()
    result = Tables(db).get_hired_employees()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))