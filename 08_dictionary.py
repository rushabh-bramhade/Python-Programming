student = {
    "firstname" : "Rushbah",
    "lastname" : "Bramhade",
    "rollno" : 20,
    "exam_enroll" : True,
    "rank" : 1,
}

# print(student)
# print(student.keys())
# print(student.get("firstname") + " "+ student.get("lastname"))
print(student.pop("rank"))
# print(student)
# print(student.values())
# print(student.items())
# print(student.clear())
print(student.update({"lastname" : "dj"}))
print(student)


students = {
    "student1": {
        "name": "Rushabh",
        "age": 20,
        "course": "Python"
    },
    "student2": {
        "name": "Amit",
        "age": 21,
        "course": "Java"
    },
    "student3": {
        "name": "Sneha",
        "age": 19,
        "course": "Data Science"
    }
}

print(students)

