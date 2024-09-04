import requests

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
response = requests.get(url)
with open('iris.csv', 'wb') as file:
    file.write(response.content)