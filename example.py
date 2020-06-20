from pymongo import MongoClient
from sklearn import datasets

import numpymongo as npm

iris = datasets.load_iris()
client = MongoClient()
db = client["test"]

db["databases"].insert_one({
    "database": "iris",
    "data": npm.from2d(iris.data),
    "target": npm.from1d(iris.target)
})

docs = []
for X, y in zip(iris.data, iris.target):
    docs.append({
        "X": npm.from1d(X),
        "y": npm.fromFloat(y)
    })

db["iris"].insert_many(docs)
