import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:home@cluster0.idizm.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client["Inventory"]
collection = database["Table1"]

records = collection.find()

for i in records:
    print(i)