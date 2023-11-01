#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
import joblib
import pandas as pd

# In[5]:


def load():
    loaded_model = joblib.load('model.pkl')
    return loaded_model


# In[6]:


st.title('Loan Eligibility Predictor')


# In[7]:


gender = st.selectbox("GENDER",('Male','Female'))
married = st.selectbox("ARE YOU MARRIED?",('Yes','No'))
dependents = st.selectbox("DEPENDENTS: ",('0','1'))
education = st.selectbox("ARE YOU GRADUATE?",('Yes','No'))
self_employed = st.selectbox("ARE YOU WORKING?",('Yes','No'))
applicant_income = st.number_input("APPLICANT INCOME")
coapplicant_income = st.number_input("COAPPLICANT INCOME")
loan_amount = st.number_input("LOAN AMOUNT")
loan_amount_term = st.selectbox("LOAN AMOUNT TERM",('12','36','60','84','120','180','300','360','480'))
credit_history = st.selectbox("CREDIT HISTORY",('0','1'))
property_area = st.selectbox("PROPERTY AREA",('Rural','Semiurban','Urban'))

data = pd.DataFrame({'Gender':gender,'Married':married,'Dependents':dependents,'Education':education,'Self_Employed':self_employed,'Applicant_income':applicant_income,'Coapplicant_income':coapplicant_income,'Loan_amount':loan_amount,'Loan_amount_term':loan_amount_term,'Credit_history':credit_history,'Property_Area':property_area}, index = [0])

data['Gender'] = data['Gender'].replace(('Male','Female'),(1,0))
data['Married'] = data['Married'].replace(('Yes','No'),(1,0))
data['Education'] = data['Education'].replace(('Yes','No'),(1,0))
data['Self_Employed'] = data['Self_Employed'].replace(('Yes','No'),(1,0))
data['Property_Area'] = data['Property_Area'].replace(('Urban','Semiurban','Rural'),(1,1,0))
data['Dependents'] = data['Dependents'].replace(('0','1'),(0,1))

if st.button('SUBMIT'):
    model = load()
    prediction = model.predict(data.values)
    if prediction == 0:
        st.write("Sorry, You are not eligible for a Loan.")
    else:
        st.write("Congrats! You are eligible for a loan.")
# In[ ]:




