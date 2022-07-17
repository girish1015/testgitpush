import pymongo
client = pymongo.MongoClient("mongodb+srv://girish1015:Ka023915@girish1015.yhsgo.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "Girish",
    "EmailID" : "girish1015@gmail.com",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
