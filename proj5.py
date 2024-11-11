import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

print("Question 1")
print("Part (b)")
hittersDF = pd.read_csv("Hitters.csv", sep=",").dropna()
hPredict = hittersDF.drop(columns=['Salary'])

