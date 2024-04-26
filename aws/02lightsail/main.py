from fastapi import FastAPI, HTTPException

import numpy as np
import joblib
import xgboost as xgb
import json

xg_model_1 = joblib.load('xg_model.pkl')

#lv = [2, 0.595, 0.475, 0.150, 0.9145, 0.3755, 0.2055, 0.2500]
#array_values = np.array(lv)
#print("*******************************************************")
#print(xg_model_1.predict([array_values])[0])

app = FastAPI()
@app.post("/")

async def process_data(data: dict):
    try:
        #print(data)

        json_data = json.dumps(data)        
        json_var = json.loads(json_data)        
        key1 = float(json_var["key1"])
        key2 = float(json_var["key2"])
        key3 = float(json_var["key3"])
        key4 = float(json_var["key4"])
        key5 = float(json_var["key5"])
        key6 = float(json_var["key6"])
        key7 = float(json_var["key7"])
        key8 = float(json_var["key8"])
        
        lv = [key1,key2,key3,key4,key5,key6,key7,key8]        
        array_values = np.array(lv)
        predict = xg_model_1.predict([array_values])[0]
        print(predict)        
        result = {"answer": "Reply: "+ str(predict)}
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))