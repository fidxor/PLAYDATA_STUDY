import seaborn as sns
import pandas as pd
from sklearn.preprocessing import LabelEncoder

iris = sns.load_dataset('iris')

x = iris.drop('species', axis = 1)
y = iris['species']

encoder = LabelEncoder()
y = encoder.fit_transform(y)

print(y)


