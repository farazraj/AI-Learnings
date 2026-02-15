def tsk1(name: str, age: int, skills: list[str]) -> dict:
    return {
        "name": name,
        "age": age,
        "skills": skills
    }

# print(tsk1('Raj', 28, ['coding', 'ai']))


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'message':'Hello justt trying'}


@app.get("/qnt/")
def hello1(st: str, qnt: int ):
    return {"Item":st,"number":qnt}



#Using pydantic
from pydantic import BaseModel

class Employee(BaseModel):
    name:str
    age:int
    skills:list[str]


@app.post("/create/")
def create_emp(emp:Employee):
    return {'Mesaage':'Employee Created',
            "data":emp 
            }


@app.post("/create_res/", response_model = Employee)
def create_emp(emp:Employee):
    return emp
