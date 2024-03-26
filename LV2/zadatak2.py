#Zadatak 2.4.2 Datoteka data.csv sadrži mjerenja visine i mase provedena na muškarcima i
#ženama. Skripta zadatak_2.py uˇcitava dane podatke u obliku numpy polja data pri ˇcemu je u
#prvom stupcu polja oznaka spola (1 muško, 0 žensko), drugi stupac polja je visina u cm, a tre´ci
#stupac polja je masa u kg.

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data.csv', skiprows=1, delimiter=',')
print(len(data))

visina = np.array(data[:,1])
masa = np.array(data[:,2])
plt.figure()
plt.scatter(visina,masa)
plt.xlabel('visina')
plt.ylabel('masa')
plt.title('Odnos visine i mase')


visina2 = visina[::50]
masa2 = masa[::50]
plt.figure()
plt.scatter(visina2,masa2)
plt.xlabel('visina')
plt.ylabel('masa')
plt.title('Odnos visine i mase svaka 50 osoba')
plt.show()
