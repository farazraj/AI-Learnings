from fastapi import FastAPI, Form, Request
from pydantic import BaseModel
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

# Load the trained model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


# Define input schema
class MessageInput(BaseModel):
    message: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5500"] etc.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Spam Classifier API is running!"}

#call the model using JSON input
@app.post("/predict_json")
def predict_spam(data: MessageInput):
    vec_msg = vectorizer.transform([data.message])
    prediction = model.predict(vec_msg)[0]
    return {
        "prediction": "Spam Message" if prediction == 1 else "Genuine Message"
    }


# Call the model using form data
@app.post("/predict_form")
def predict(message: str = Form(...)):
    vec_msg = vectorizer.transform([message])
    pred = model.predict(vec_msg)[0]
    result = "Spam Message" if pred == 1 else "Genuine Message"
    return {"prediction": result}



# Call the model using either JSON or form data
@app.post("/predict_json_or_form")
async def predict(request: Request, message: str = Form(None)):
    if request.headers.get("content-type", "").startswith("application/json"):
        data = await request.json()
        message = data.get("message")
    elif message is None:
        return {"error": "No message provided"}

    vec_msg = vectorizer.transform([message])
    pred = model.predict(vec_msg)[0]
    result = "Spam Message" if pred == 1 else "Genuine Message"
    return {"prediction": result}