import csv
with open("EmployeePay.csv","r") as inputfile:
    reader = csv.reader(inputfile)

    for row in reader:
        idnum = row [0]
        firstname = row [1]
        lastname = row [2]
        salary = row [3]
        bonus = row [4]

        print(f"id: {idnum}")
        print(f"first name: {firstname}")
        print(f"last name: {lastname}")
        print(f"salary: {salary}")
        print(f"bonus: {bonus}")
        print()