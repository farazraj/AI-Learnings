from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

#Dependancy injection sample
def get_current_user():
    return {"username":"admin"}

@app.get("/profile/")
def profile(user=Depends(get_current_user)):
    return user


#task:Create a dependency:

def verify_token(token: str):
    if token != "secret":
        raise HTTPException(status_code=401, detail="Invalid token")
    else:
        return {"Message":"Valid token", "token":token}

@app.get('/auth/')
def auth_token(val = Depends(verify_token)):
    return val

#sync and async 

#CPU bound for CPU heavy tasks like ML pediction
@app.get("/sync")
def sync_route():
    return {"type": "sync"}

#Majorly used for: 
# Calling external API

# Reading file

# DB I/O

# Waiting on network
@app.get("/async")
async def async_route():
    return {"type": "async"}


#file upload - useful for AI jobs

from fastapi import UploadFile, File

@app.post("/upload/")
async def upload_file(file:UploadFile = File(...)):
    return {"filename":file.filename,
            "content_type":file.content_type}


@app.post("/readup/")
async def read_upload(file:UploadFile = File(...)):
    content = await file.read()
    return {"size":len(content),
        "content":content.decode()}


#background tasks

from fastapi import BackgroundTasks
import time

def write_log(message:str):
    with open("log.txt", "a") as f:
        f.write(message)

@app.post("/process/")
def process_back(back_task:BackgroundTasks, y:int):
    if y == 1:
        back_task.add_task(write_log, "Processing Start\n")
        time.sleep(5)
        back_task.add_task(write_log, "Processing done\n")
        return{"message":"Task Started/Complete"}
    else:
        back_task.add_task(write_log, "Not Started\n")
        return{"message":"Task failed"}

    


"""
Mini “Resume Analyzer API” (no AI yet)

Endpoints:

Upload resume file

Fake analyze (count words)

Return word count

Use BackgroundTask to save log

Protect endpoint with simple token dependency

"""

from datetime import datetime
from fastapi import Header

def sec_tok(token:str= Header(...)):
    if token != 'top':
        raise HTTPException(status_code = 401, detail="Invalid token")
    

def write_log1(message:str):
    with open("up_log.txt","a") as f:
        f.write(message)

@app.post("/res_analyse/")
async def resume_analyser(bt:BackgroundTasks, tok = Depends(sec_tok),file:UploadFile = File(...)):
    content = await file.read()
    # try:
    #     text = content.decode("utf-8")
    # except:
    #     raise HTTPException(status_code = 400, detail = "File must be text based")
    bt.add_task(write_log1, f"Date : {datetime.now()}, filename:{file.filename}, words:{len(content.split())}\n")
    return {"Message":"Analysing Done"}

