import pandas as pd
import csv

df = pd.read_csv("totalStars.csv")
print(df.shape)

df = df.rename({
    "Star_name":"temp_Star_name",
    "Distance":"temp_Distance",
    "Mass":"temp_Mass",
    "Radius":"temp_Radius"
})

del df["Luminosity"]
del df["Star_name.1"]
del df["Distance.1"]
del df["Mass.1"]
del df["Radius.1"]
del df["Unnamed: 0"]
del df["Unnamed: 9"]

print(df.shape)

df.to_csv("final.csv")