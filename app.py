from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from schema.UserInfo import UserInfo
from model.predict import predict_insurance_premimium, MODEL_VERSION


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Insurance Premium Prediction API"}

@app.get("/health")
def health_check():
    return {"status": "ok",
            "version": MODEL_VERSION}


@app.post("/predict")
def predict(data: UserInfo):
    try:
    # takes only the required parameters for the model and also convert it into dictionary
        input_df ={
            'bmi': data.bmi,
            'age_group': data.age_group,
            'lifestyle_risk': data.lifestyle_risk,
            'city_tier': data.city_tier,
            'income_lpa': data.income_lpa,
            'occupation': data.occupation
        }
        # making prediction of the model and saving it in the prediction variable        
        prediction = predict_insurance_premimium(input_df)

        # sending the json response if success
        return JSONResponse(status_code=200, content={'predicted_insurance_premium': prediction[0]})
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", reload=True)