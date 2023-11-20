from sqlalchemy import Boolean, Column, Integer, String
from database.database import Base

class HiredEmployees(Base):
    __tablename__ = "hired_employees"

    id = Column(Integer, primary_key = True, index = True)
    id_hired_employees = Column(String)
    name = Column(String)
    datetime = Column(String)
    department_id = Column(String)
    job_id = Column(String)


class Departments(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key = True, index = True)
    id_departments = Column(Integer)
    department = Column(String)


class Jobs(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key = True, index = True)
    id_jobs = Column(Integer)
    job = Column(String)



class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
