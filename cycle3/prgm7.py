import pandas as pd
df=pd.read_csv('iris.csv')
print("Shape of the dataset is :",df.shape)
print("First 5 and last Five rows of the data set\n",df)
print("Size of the dataset:",df.size)
print("No. of Samples available for each variety\n",df.count())
print("Description of the Dataset\n",df.describe())