from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017/')

db = client['studentList']

table = db['stdInfo']

print("db is connected")

# for s in table.find():
#     print(s)


# insert
# newStudent =[{"name":"raja","rollNo":"111AI010","city":"Erode"},{"name":"Deepa","rollNo":"111AI011","city":"CBE"}]
# table.insert_many(newStudent)


# update
# table.update_one({"rollNo":"111AI009"},{'$set':{"city":"CBE"}})
# print("Data updated successfully")

# delete
table.delete_one({"rollNo":"111AI009"})
print("user deleted succesfully")