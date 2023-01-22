import pymongo

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.kirb2v7.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

collection = db.students

student_list = collection.find({})

print("\n --DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print (" Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

result = collection.update_one({"student_id": "1007"}, {"$set": {"last_name": "TheBlue"}})

gandalf = collection.find_one({"student_id": "1007"})

print("\n --DISPLAYING STUDENT DOCUMENT 1007 --")

print(" Student ID: " + gandalf["student_id"] + "\n First Name: " + gandalf["first_name"] + "\n Last Name: " + gandalf["last_name"] + "\n")

input("\n\n End of program, press any key to continue...")