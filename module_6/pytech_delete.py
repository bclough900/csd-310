import pymongo

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.kirb2v7.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

collection = db.students

student_list = collection.find({})

print("\n --DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY  --")

for doc in student_list:
     print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

new_doc = {
    "student_id" : "1010",
    "first_name" : "MouthOf",
    "last_name" : "Sauron",
}
new_doc_insert = collection.insert_one(new_doc).inserted_id
print("\n -- INSERT STATEMENTS -- ")
print("Inserted student record into the students collection with document_id " +  str(new_doc_insert))

student_test_doc = collection.find_one({"student_id": "1010"})
print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + student_test_doc["student_id"] + "\n  First Name: " + student_test_doc["first_name"] + "\n  Last Name: " + student_test_doc["last_name"] + "\n")


delete_student_doc = collection.delete_one({"student_id" : "1010"})
updated_student_list = collection.find({})
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in updated_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

print("\n End of program press any key to continue...")


