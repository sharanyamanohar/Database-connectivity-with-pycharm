import pymongo
client = pymongo.MongoClient("mongodb+srv://sharanya:urpassword@sharanya.30gyscv.mongodb.net/?retryWrites=true&w=majority")
#mongodb is a password don't use special character
db = client.test
print(db)
d={"name":"sara",
    "emailid":"sara@gmail.com",
    "surname":"nadar"}
db2=client['mongotest']#creating a newdb so it is named as db2
call=db2['test']
call.insert_one(d)#inserting only one dictionary

db3=client['myinfo']
coll=db3['sara_test']
coll.insert_one(d)

#the same databases will be available by clicking the link
