# -*- coding: utf-8 -*-
"""credit_score_classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Kak0XvI7DRyXsyRC23PjDdbm_OYiT02m
"""

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"

data = pd.read_csv("train.csv")
data.head()

data = data.dropna()

data.info()

data.isnull().sum()

data["Credit_Score"].value_counts()

fig = px.box(data,
           x="Occupation",
           color="Credit_Score",
           title="Credit Scores Based on Occupation",
           color_discrete_map={'Poor':'red',
                               'Standard':'yellow',
                               'Good':'green'})
fig.show()

fig=px.box(data,
           x="Occupation",
           y="Annual_Income",
           color="Credit_Score",
           title="Credit Scores Based on Annual Income",
           color_discrete_map={'Poor':'red',
                               'Standard':'yellow',
                               'Good':'green'},
           )
fig.update_traces(quartilemethod="exclusive")
fig.show()

fig = px.box(data,
           x="Occupation",
           y="Monthly_Inhand_Salary",
           color="Credit_Score",
           title="Credit Scores Based on Occupation",
           color_discrete_map={'Poor':'red',
                               'Standard':'yellow',
                               'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

fig = px.box(data,
           x="Occupation",
           y="Num_Bank_Accounts",
           color="Credit_Score",
           title="Credit Scores Based on Occupation",
           color_discrete_map={'Poor':'red',
                               'Standard':'yellow',
                               'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

fig = px.box(data,
           x="Occupation",
           y="Num_Credit_Card",
           color="Credit_Score",
           title="Credit Scores Based on Occupation",
           color_discrete_map={'Poor':'red',
                               'Standard':'yellow',
                               'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

fig = px.box(data,
           x="Occupation",
           y="Interest_Rate",
           color="Credit_Score",
           title="Credit Scores Based on Occupation",
           color_discrete_map={'Poor':'red',
                               'Standard':'yellow',
                               'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

fig = px.box(data,
           x="Occupation",
           y="Num_of_Loan",
           color="Credit_Score",
           title="Credit Scores Based on Occupation",
           color_discrete_map={'Poor':'red',
                               'Standard':'yellow',
                               'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

fig = px.box(data,
           x="Occupation",
           y="Delay_from_due_date",
           color="Credit_Score",
           title="Credit Scores Based on Occupation",
           color_discrete_map={'Poor':'red',
                               'Standard':'yellow',
                               'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

fig = px.box(data,
           x="Occupation",
           y="Num_of_Delayed_Payment",
           color="Credit_Score",
           title="Credit Scores Based on Occupation",
           color_discrete_map={'Poor':'red',
                               'Standard':'yellow',
                               'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

fig = px.box(data,
           x="Occupation",
           y="Credit_Mix",
           color="Credit_Score",
           title="Credit Scores Based on Occupation",
           color_discrete_map={'Poor':'red',
                               'Standard':'yellow',
                               'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

fig = px.box(data,
           x="Occupation",
           y="Outstanding_Debt",
           color="Credit_Score",
           title="Credit Scores Based on Occupation",
           color_discrete_map={'Poor':'red',
                               'Standard':'yellow',
                               'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

fig = px.box(data,
           x="Occupation",
           y="Credit_History_Age",
           color="Credit_Score",
           title="Credit Scores Based on Occupation",
           color_discrete_map={'Poor':'red',
                               'Standard':'yellow',
                               'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

fig = px.box(data,
           x="Occupation",
           y="Monthly_Balance",
           color="Credit_Score",
           title="Credit Scores Based on Occupation",
           color_discrete_map={'Poor':'red',
                               'Standard':'yellow',
                               'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

data["Credit_Mix"] = data["Credit_Mix"].map({"Standard": 1,
                               "Good": 2,
                               "Bad": 0})

from sklearn.model_selection import train_test_split
x=np.array(data[["Annual_Income", "Monthly_Inhand_Salary",
                   "Num_Bank_Accounts", "Num_Credit_Card",
                   "Interest_Rate", "Num_of_Loan",
                   "Delay_from_due_date", "Num_of_Delayed_Payment",
                   "Credit_Mix", "Outstanding_Debt",
                   "Credit_History_Age", "Monthly_Balance"]])
y=np.array(data[["Credit_Score"]])

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.33,random_state=42)
from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier()
model.fit(xtrain,ytrain)

print("Credit Score Prediction : ")
a = float(input("Annual Income: "))
b = float(input("Monthly Inhand Salary: "))
c = float(input("Number of Bank Accounts: "))
d = float(input("Number of Credit cards: "))
e = float(input("Interest rate: "))
f = float(input("Number of Loans: "))
g = float(input("Average number of days delayed by the person: "))
h = float(input("Number of delayed payments: "))
i = input("Credit Mix (Bad: 0, Standard: 1, Good: 3) : ")
j = float(input("Outstanding Debt: "))
k = float(input("Credit History Age: "))
l = float(input("Monthly Balance: "))

features = np.array([[a, b, c, d, e, f, g, h, i, j, k, l]])
print("Predicted Credit Score = ", model.predict(features))

#Classifying customers based on their credit scores helps banks and credit card companies immediately to issue loans to
# customers with good creditworthiness.
# A person with a good credit score will get loans from any bank and financial institution.
# I hope you liked this article on Credit Score Classification with Machine Learning using Python.