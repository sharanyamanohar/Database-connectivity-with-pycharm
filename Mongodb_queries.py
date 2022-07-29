import pymongo
client = pymongo.MongoClient("mongodb+srv://sharanya:urpassword@sharanya.30gyscv.mongodb.net/?retryWrites=true&w=majority")
#mongodb is a password don't use special character
db = client.test
print(db)
d=[
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]
database = client['inventory']
collection = database["table"]
collection.insert_many(data)#many kind of dictionary is stored in one list so its written in insert_many


#Queries begins comment out and check it

#d = collection.find({'status':'A'})
#d = collection.find({'status':{'$in':['A' , 'P']}})
#d = collection.find({'status':{"$gt" : "C"}})
#d = collection.find({'qty':{'$gte' :75}})
#d = collection.find({'item': 'sketch pad','qty': 95})
#d = collection.find({ 'item': 'sketch pad' , 'qty' :{"$gte" : 75}})
#d = collection.find({'$or' : [{ 'item': 'sketch pad'} , {'qty': {"$gte": 75}}]})
#collection.update_one({'item': 'canvas'} , {'$set':{'item': 'sharanya'} })
collection.delete_one({'item': 'sharanya'})
d = collection.find({'item': 'sharanya'})

for i in d :#for interating every elements on d
    print(i)
