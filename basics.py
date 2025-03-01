import streamlit as st
import time as t
import pickle
import numpy as np



loaded_model=pickle.load(open('c:/Users/naras/Downloads/trained_model.sav','rb'))



def diabetes_predection(input_data):    
    input_data_as_numpy_array=np.asanyarray(input_data)
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    predection=loaded_model.predict(input_data_reshaped)
    print(predection)

    if(predection==0):
        return "NOT DIABETIC"
    else:
        return "DAIBETIC"
    


def main():
    st.title("DIABETES PREDECTION")
    pregnancies=st.number_input("PREGNANCIES")
    glucose=st.number_input("GLUCOSE LEVEL ",max_value=200)
    bloodpressure=st.number_input("BLOOD PRESSURE ",max_value=80)
    skinthickness=st.number_input("SKIN THICKNESS",max_value=50)
    insulin =st.number_input("INSULIN ",max_value=1000)
    bmi=st.number_input("BMI",max_value=80.0)
    diabetespedigreefunction=st.number_input("ENETR DIABETES PEDIGREE FUNCTION",min_value=0.0)
    age=st.number_input("ENETR YOUR AGE",min_value=1)


    diagnosis=''
    if st.button('DIABETES TEST RESULT'):
        diagnosis=diabetes_predection([pregnancies,glucose,bloodpressure,skinthickness,insulin,bmi,diabetespedigreefunction,age])
    
    st.success(diagnosis)
if __name__=='__main__':
    main()








