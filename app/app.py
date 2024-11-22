from fastapi import FastAPI, Request, Form
import pickle
import numpy as np
from pydantic import BaseModel
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Load the model and scaler
# regmodel = pickle.load(open('reg_model.pkl', 'rb'))
# scalar = pickle.load(open('scaling.pkl', 'rb'))

regmodel = pickle.load(open('app/reg_model.pkl', 'rb'))
scalar = pickle.load(open('app/scaling.pkl', 'rb'))

#Initialize Fastapi app
app = FastAPI()

# Set up Jinja2 for HTML rendering
templates = Jinja2Templates(directory="app/templates")

# Mount the images directory as a static directory
# app.mount("/images", StaticFiles(directory="images"), name="images")
app.mount("/images", StaticFiles(directory="app/images"), name="images")

# Define input structure for prediction
class PredictionRequest(BaseModel):
    SepalLengthCm: float
    SepalWidthCm: float
    PetalLengthCm: float
    PetalWidthCm: float

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/predict")
async def predict_form(
    SepalLengthCm: float = Form(...),
    SepalWidthCm: float = Form(...),
    PetalLengthCm: float = Form(...),
    PetalWidthCm: float = Form(...)
):
    # Use the form data to create a PredictionInput instance
    input_data = PredictionRequest(
        SepalLengthCm=SepalLengthCm,
        SepalWidthCm=SepalWidthCm,
        PetalLengthCm=PetalLengthCm,
        PetalWidthCm=PetalWidthCm
    )

    # Process the input data (scaling and prediction)
    data = input_data.model_dump()  # Convert Pydantic model to dictionary

    # scaled_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))
    scaled_data = np.array(list(data.values())).reshape(1, -1)
    output = regmodel.predict(scaled_data)[0]

    print(output)
    # Define the mapping from output to flower names
    flower_mapping = {0: 'setosa', 1: 'versicolor ', 2: 'virginica '}

    # Display the prediction result
    return templates.TemplateResponse(
        "home.html", 
        {"request": {}, "prediction_text": f"The Flower prediction is {flower_mapping.get(output)}"}
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
