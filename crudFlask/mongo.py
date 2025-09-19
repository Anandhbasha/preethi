from pymongo import MongoClient
from pymongo.errors import WriteError

client = MongoClient('mongodb://127.0.0.1:27017/')

db = client['studentList']



# for s in table.find():
#     print(s)


# insert
# newStudent =[{"name":"raja","rollNo":"111AI010","city":"Erode"},{"name":"Deepa","rollNo":"111AI011","city":"CBE"}]
# table.insert_many(newStudent)


# update
# table.update_one({"rollNo":"111AI009"},{'$set':{"city":"CBE"}})
# print("Data updated successfully")

# delete
# table.delete_one({"rollNo":"111AI009"})
# print("user deleted succesfully")



db.command({
        "collMod":"stdInformation",
        "validator":{
                '$jsonSchema':{
                "bsonType":"object",
                "required":["name","rollNo","city"],
                "properties":{
                    "name":{
                        "bsonType":"string",
                        "desc":"Name must be a String and required"
                    },
                    "rollNo":{
                        "bsonType":"string",
                        "pattern":"^[0-9]{3}[A-Z]{2}[0-9]{3}$",
                        "desc":"RollNo must be a String and required"
                    },
                    "city":{
                        "bsonType":"string",
                        "desc":"City must be a String and required"
                    }
                }
            }
        },
    "validationLevel":"strict"
}
) 


table = db['stdInformation']

print("db is connected")


# insert 

try:
    newStudent = {"name":"Deepa","rollNo":"1111","city":"Chennai"}
    table.insert_one(newStudent)
    print("Data inserted Succesfully")
except WriteError as e:
    print("Insert Failed")