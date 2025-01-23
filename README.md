# **Predictive Analysis for Manufacturing Operations**



### **Set up Instructions:**



#### Follow these steps to set up and run the project:


### **1.Install Dependencies**
#### Use the provided requirements.txt file to install all necessary dependencies:

    
    pip install -r requirements.txt  

### **2.Run the API**
#### Navigate to the `python_code` folder and run the `ml_api.py` file using the following command in your terminal:
    
    uvicorn python_code.ml_api:app --reload  


### **3.Access the API**
#### After running the above command, the API will be accessible locally.


### **4.Test the Endpoint**
#### You can test the model using the `/machine_prediction` endpoint with tools like **Restfox** or **Postman**:

+ URL: `http://127.0.0.1:8000/machine_prediction`
+ Use a POST request to interact with the API and view predictions.



### **Features**
+ #### Predicts machine status (working or failure) using ML models
+ #### RESTful API built using FastAPI.
+ #### Local endpoint for quick access and testing.


### **Example Request**
#### Here’s an example of a POST request to the `/machine_prediction` endpoint:

    
    {
     "air_temperature_K": 300.0,
     "process_temperature_K": 310.0,
     "rotational_speed_rpm": 1500,
     "torque_Nm": 40.0,
     "tool_wear_min": 10
    }
#### Response: 
+ If Machine Fails: `"There is a Machine Failure"`
+ If Machine Works: `"The Machine is working"`




