from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv('data_C02_emission.csv')

#a

X = dataframe[['Engine Size (L)', 'Cylinders', 'Fuel Consumption City (L/100km)', 'Fuel Consumption Hwy (L/100km)', 'Fuel Consumption Comb (L/100km)', 'Fuel Consumption Comb (mpg)']]
y = dataframe['CO2 Emissions (g/km)']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

#b

plt.figure()
plt.scatter(y_train, X_train['Fuel Consumption City (L/100km)'], color="blue", s=10, alpha=0.5)
plt.scatter(y_test, X_test['Fuel Consumption City (L/100km)'], color = "red", s=10, alpha=0.5)
plt.show()

#c


sc = MinMaxScaler()
X_train_n =sc.fit_transform(X_train)
scaled_X_train =pd.DataFrame(X_train_n, columns = X_train.columns)
scaled_X_test = pd.DataFrame(X_train_n, columns = X_train.columns)

X_train['Fuel Consumption City (L/100km)'].plot(kind="hist", bins = 25)
plt.show()
scaled_X_train['Fuel Consumption City (L/100km)'].plot(kind="hist", bins = 25)
plt.show()

