import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credit = pd.read_csv('credit_data.csv')
# print(base_credit.head(10))
# print(base_credit.tail(10))
# print(base_credit[base_credit['income'] >= 69995.685578])
# print(base_credit[base_credit['loan'] <= 1.377630])

print(np.unique(base_credit['default'], return_counts=True))
# print(sns.countplot(x = base_credit['default']))
def grafic_default():
    sns.countplot(x=base_credit['default'])
    plt.show()
# print(grafic_default())
def histogram_age():
    plt.hist(x=base_credit['age'])
    plt.show()
# print(histogram())
def histogram_income():
    plt.hist(x=base_credit['income'])
    plt.show()
# print(histogram_income())
def histogram_loan():
    plt.hist(x=base_credit['loan'])
    plt.show()
# print(histogram_loan())
def grafico_geral():
    grafico = px.scatter_matrix(base_credit, dimensions=['age', 'income', 'loan'], color='default')
    grafico.show()
# print(grafico_geral())