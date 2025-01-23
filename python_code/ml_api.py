import sklearn
from fastapi import FastAPI
from pydantic import BaseModel, Field
import pickle 
import json 

app = FastAPI() 

from pydantic import BaseModel, Field

class ModelInput(BaseModel):
    air_temperature_K: float = Field(..., alias="Air temperature [K]")
    process_temperature_K: float = Field(..., alias="Process temperature [K]")
    rotational_speed_rpm: int = Field(..., alias="Rotational speed [rpm]")
    torque_Nm: float = Field(..., alias="Torque [Nm]")
    tool_wear_min: int = Field(..., alias="Tool wear [min]")


prediction_model = pickle.load(open("C:\\Users\\hp\\Desktop\\College\\Predictive Analysis for Manufacturing Operations\\python_code\\pipe.pkl", "rb"))



@app.post('/machine_prediction')
def machine_pred(input_parameters : ModelInput):

    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)


    air_temp = input_dictionary['air_temperature_K']
    process_temp = input_dictionary['process_temperature_K']
    rpm = input_dictionary['rotational_speed_rpm']
    torque = input_dictionary['torque_Nm']
    tool_wear = input_dictionary['tool_wear_min']


    input_list = [air_temp,process_temp,rpm,torque,tool_wear]

    prediction = prediction_model.predict([input_list])


    if prediction[0] == 0:
        return 'There is a Machine Failure'
    
    else:

        return 'The Machine is working'






