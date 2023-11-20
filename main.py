from fastapi import FastAPI
import models.models as model
from database.database import engine
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "Data Engineer Code Challenge"
app.version = "0.0.1"

model.Base.metadata.create_all(bind = engine)

# API path
@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>API Online</h1>')
