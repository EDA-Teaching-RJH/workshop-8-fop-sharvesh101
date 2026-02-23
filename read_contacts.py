import csv

with open("contacts.csv","r") as file:
    reader = csv.DictReader(file,delimiter=",")
    for line in reader:
        print(f"Name : {line["name"]:<20}  Email : {line["email"]}")