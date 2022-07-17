import pymongo

client = pymongo.MongoClient("mongodb+srv://home:ka023915@cluster0.yhsgo.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

data = {"name": 'girish', "EmailID":"girish1015@gmail.com",  "surname":"kumar"}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(data)
