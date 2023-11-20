from fastapi import FastAPI
import models.models_tables as model
from database.database import engine
from fastapi.responses import HTMLResponse
from routers.tables import tables_router
from routers.auth import auth_router

app = FastAPI()
app.title = "Data Engineer Code Challenge"
app.version = "0.0.1"

# Routers
app.include_router(tables_router)
app.include_router(auth_router)

# Create tables
model.Base.metadata.create_all(bind = engine)

# API path
@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>API Online</h1>')
