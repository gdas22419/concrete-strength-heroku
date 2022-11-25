from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

origin=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origin=origins,
    allow_credential=True,
    allow_methods=['*'],
    allow_header=['*']
)
class model_input(BaseModel):

    Cement : float
    Blast_Furnace_Slag : float
    Fly_Ash : float
    Water : float
    Superplasticizer : float
    Coarse_aggregate : float
    Fine_Aggregate : float
    Age : int

# loading the saved model
loaded_model = pickle.load(open('trained_model.sav','rb'))

@app.post('/trained_model')
def strength_predd(input_parameters:model_input):

    input_data=input_parameters.json()
    input_dictionary=json.loads(input_data)

    cement = input_dictionary['Cement']
    Blast_Furnace = input_dictionary['Blast_Furnace_Slag']
    fly_Ash = input_dictionary['Fly_Ash']
    water = input_dictionary['Water']
    superplasticizer = input_dictionary['Superplasticizer']
    coarse_aggregate = input_dictionary['Coarse_aggregate']
    fine_Aggregate = input_dictionary['Fine_Aggregate']
    age = input_dictionary['Age']

    input_list = [cement,Blast_Furnace,fly_Ash,water,superplasticizer,coarse_aggregate,fine_Aggregate,age]
    prediction=loaded_model.predict([input_list])

    return prediction

