import csv
from config import file_name

def getallcont():
    cont = []
    with open(file_name,'r') as file:
        read = csv.DictReader(file)
        for row in read:
            cont.append(row)
    return cont

def addnewcont(name,phone):
    with open(file_name,'a') as file:
        file.write(f"\n{name},{phone}")

def delperson(name='0',phone='0'):
    cont = []
    with open(file_name,'r') as file:
        read = csv.DictReader(file)
        for i in read:
            if (name == i['name'] and name !='0') or (phone == i['phone'] and phone !='0'):
                continue
            else:
                cont.append(i)

    with open(file_name, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "phone"])
        writer.writeheader()
        writer.writerows(cont)
        
    return cont



