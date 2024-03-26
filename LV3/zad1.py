import pandas as pd

#a

data = pd.read_csv('data_C02_emission.csv')
print(data.count())
print(data.info())
print ( data . isnull () . sum () )
data . dropna ( axis =0 )
data . dropna ( axis =1 )
data . drop_duplicates ()
data = data . reset_index ( drop = True )

#b 

data.sort_values(by = ['Fuel Consumption City (L/100km)'])
print('Najveća potrošnja:\n', data[['Make','Model','Fuel Consumption City (L/100km)']].tail(3))
print('Najmanja potrošnja:\n', data[['Make','Model','Fuel Consumption City (L/100km)']].head(3))

#c
#Koliko vozila ima velicinu motora izme ˇ du 2.5 i 3.5 L? 
#Kolika je prosje ¯ cna C02 emisija ˇplinova za ova vozila?

print(len(data[(data['Engine Size (L)'] >= 2.5) & (data['Engine Size (L)'] <= 3.5)]))

nova_data=(data[(data['Engine Size (L)'] >= 2.5) & (data['Engine Size (L)'] <= 3.5)])
print(nova_data['CO2 Emissions (g/km)'].mean())