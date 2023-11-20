from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class HiredEmployees(Base):
    __tablename__ = "hired_employees"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    datetime = Column(String)
    department_id = Column(Integer, ForeignKey("departments.id"))
    job_id = Column(Integer, ForeignKey("jobs.id"))

    jobs = relationship("Jobs", back_populates = "employee_job")
    departments = relationship("Departments", back_populates = "employee_department")


class Departments(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key = True, index = True)
    department = Column(String)

    employee_department = relationship("HiredEmployees", back_populates = "departments")

class Jobs(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key = True, index = True)
    job = Column(String)

    employee_job = relationship("HiredEmployees", back_populates = "jobs")
