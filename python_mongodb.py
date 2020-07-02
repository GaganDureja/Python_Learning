import pymongo
# make connection to localhost
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
# create database
mongodb = myclient['students']
# create colloection --table
mycol = mongodb['students_info']
mycol1 = mongodb['students_info1']
# insert data
"""mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
] # if we don't specify id the mongodb will create on its own for every entry
# use insert_one for one entry
x = mycol.insert_many(mylist)
x = mycol1.insert_many(mylist)
#print a list of the _id values of the inserted documents:
print(x.inserted_ids)"""

print('List of databases:')
print(myclient.list_database_names())

print('List of collections:')
print(mongodb.list_collection_names())

# find some column
print("return some columns from colloection:")
for x in mycol.find({},{"_id":0, "name": 1, "address": 1 }).limit(5):
  print(x)
# find all
print("return complete colloection data:")
for x in mycol.find():
  print(x)
# find one
print("return the first row:")
x = mycol.find_one()
print(x)

# filter search
print("Search with address Park lane:")
myquery = { "address": "Park Lane 38" }
mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
# advance query 
print("Search starting with S or greater alphabet")
myquery = { "address": { "$gt": "S" } }# case sensitive
mydoc = mycol.find(myquery)
for x in mydoc:
	print(x)

# filter with regular expression
print("Address start with S")
myquery = { "address": { "$regex": "^S" }}
mydoc = mycol.find(myquery)
for x in mydoc:
	print(x)

# Sort
print("Sort descending names")
mydoc = mycol.find().sort("name", -1)
for x in mydoc:
	print(x)

# Delete data from collection
print("delete rows")
myquery = { "address": "Mountain 21"} 
i = mycol1.delete_one(myquery) # delete_many and for all-- delete_many({})
print(i.deleted_count, "rows deleted.")
for x in mycol1.find():
	print(x)

# Drop collection
#mycol.drop()

# Update data
myquery = { "address": {"$regex": "^M"} }
mynewval = { "$set": {"address": "New again"} }

x = mycol1.update_many(myquery, mynewval)
print(x.modified_count, "rows updated")
if x.modified_count > 0:
	for x in mycol1.find():
		print(x)
else: pass

# limit the output
# use after find().limit(5) as used above