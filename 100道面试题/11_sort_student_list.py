students = [
    {"sno": 101, "sname": "小张", "sgrade": 88},
    {"sno": 102, "sname": "小王", "sgrade": 99},
    {"sno": 103, "sname": "小李", "sgrade": 77},
    {"sno": 104, "sname": "小赵", "sgrade": 66}
]

students_sort = sorted(students, key=lambda x: x["sgrade"],reverse=False)

# print(f"source {students}, sort result:{students_sort}")

print(students_sort)
print(students)