from fastapi import FastAPI, Depends

app = FastAPI()

#Dependancy injection sample
def get_current_user():
    return {"username":"admin"}

@app.get("/profile/")
def profile(user=Depends(get_current_user)):
    return user

