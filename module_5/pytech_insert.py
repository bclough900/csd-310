import pymongo

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.kirb2v7.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

collection = db.students

students = db.students

gandalf = {
    "student_id" : "1007",
    "first_name" : "Gandalf",
    "last_name" : "TheGrey",
}

aragorn = {
    "student_id" : "1008",
    "first_name" : "Aragorn",
    "last-name" : "Strider",
}

gimli = {
    "student_id" : "1009",
    "first_name" : "Gimli",
    "last_name" : "Gloin",
}

student1 = students.insert_one(gandalf).inserted_id
student2 = students.insert_one(aragorn).inserted_id
student3 = students.insert_one(gimli).inserted_id

print("Inserted student record " + gandalf["first_name"] + " " + gandalf["last_name"] + " into the students collection with document_id " + str(student1))
print("Inserted student record " + aragorn["first_name"] + " " + aragorn["last_name"] + " into the students collection with document_id " + str(student2))
print("Inserted student record " + gimli["first_name"] + " " + gimli["last_name"] + " into the students collection with document_id " + str(student3))