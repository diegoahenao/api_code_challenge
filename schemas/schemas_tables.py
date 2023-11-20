from pydantic import BaseModel, Field

class HiredEmployeesCreate(BaseModel):
    id_hired_employees: int = Field(gt=0)
    name: str
    datetime: str
    department_id: str
    job_id: str

class DepartmentsCreate(BaseModel):
    id_departments: int = Field(gt=0)
    department: str = Field(min_length=2)

class JobsCreate(BaseModel):
    id_jobs: int = Field(gt=0)
    job: str = Field(min_length=2)

class UserCreate(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
