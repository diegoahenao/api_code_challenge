from pydantic import BaseModel, Field

class HiredEmployeesCreate(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=2)
    datetime: str
    department_id: int = Field(gt=0)
    job_id: int = Field(gt=0)

class DepartmentsCreate(BaseModel):
    id: int = Field(gt=0)
    department: str = Field(min_length=2)

class JobsCreate(BaseModel):
    id: int = Field(gt=0)
    job: str = Field(min_length=2)

class UserCreate(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
