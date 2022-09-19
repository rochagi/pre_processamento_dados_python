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

idades_negativas = base_credit.loc[base_credit['age']< 0]
# print(idades_negativas)

######### excluindo COLUNA de idade ######
base_credit2 = base_credit.drop('age', axis= 1)
# print(base_credit2)

######### excluindo LINHAS com idade negativa ########
base_credit3 = base_credit.drop(base_credit[base_credit['age'] < 0].index)
# print(base_credit3.loc[base_credit3['age']<0])

######## pegando média de idade somente das idades positivas ########
# print(base_credit['age'][base_credit['age']>0].mean())

####### colocando média de idades positivas nas idades negativas ########
base_credit.loc[base_credit['age'] < 0, 'age'] = base_credit['age'][base_credit['age']>0].mean()
# print(base_credit.head(27))

########## verificar valores faltantes ############
valores_faltantes = base_credit.isnull().sum()
# print(valores_faltantes)

########## pegando os indices com idade faltante #######
idades_faltantes = base_credit.loc[pd.isnull(base_credit['age'])]
# print(idades_faltantes)

######### corrigindo idades faltantes para média de idades ######
# base_credit.loc[pd.isnull(base_credit['age'])] = base_credit['age'][base_credit['age']>0].mean()
# print(base_credit.loc[pd.isnull(base_credit['age'])])
base_credit['age'].fillna(base_credit['age'].mean(), inplace=True)
# print(base_credit.head(33))

########## previsores
X_credit = base_credit.iloc[:, 1:4].values
# print(X_credit)
######### respostas
y_credit = base_credit.iloc[:, 4].values
# print(y_credit)

######### escalonamento de valores
print(X_credit[: , 0].min(), X_credit[:, 1].min(), X_credit[:,2].min())
print(X_credit[: , 0].max(), X_credit[:, 1].max(), X_credit[:,2].max())

from sklearn.preprocessing import StandardScaler
scaler_credit = StandardScaler()
X_credit = scaler_credit.fit_transform(X_credit)
print(X_credit[: , 0].min(), X_credit[:, 1].min(), X_credit[:,2].min())
print(X_credit[: , 0].max(), X_credit[:, 1].max(), X_credit[:,2].max())