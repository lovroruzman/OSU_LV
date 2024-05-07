import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("LV3/data_C02_emission.csv")

data["Fuel Type"] = data["Fuel Type"].astype("category")

plt.figure()
data["CO2 Emissions (g/km)"].plot(kind="hist").set_title("CO2 Emissions (g/km)")
data.plot.scatter(x="Fuel Consumption City (L/100km)", y = "CO2 Emissions (g/km)", c = "Fuel Type", cmap ="viridis")
data.boxplot(column=["Fuel Consumption Hwy (L/100km)"], by ="Fuel Type")