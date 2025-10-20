import pandas as pd
import pickle


#import ml model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

MODEL_VERSION = "1.0.0"

def predict_insurance_premium(data: dict):
    input_df = pd.DataFrame([data])
    output = model.predict(input_df)
    return output