
import connect

inp = '0'
while inp != '6':
    print('(1) get all contacts \n(2) add contact \n(3) get number of person by name \n(4) get name of person by number \n(5) delete contact \n(6)stop')
    inp = input()

    if inp == '1':
        cont = connect.getallcont()
        for i in cont:
            print(f"{i['name']} : {i['phone']}")
    
    if inp == '2':
        name = input('name: ')
        phone = input('phone number: ')
        connect.addnewcont(name,phone)

    if inp == '3':
        cont = connect.getallcont()
        name = input('name: ')
        for i in cont:
            if i['name']==name:
                print(f"{i['name']} : {i['phone']}")
                break
    
    if inp == '4':
        cont = connect.getallcont()
        number = input('phone number: ')
        for j in cont:
            if j['phone'] == number:
                print(f"{j['name']} : {j['phone']}")
                break

    if inp == '5':
        name = input('name: ')
        phone = input('phone number: ')
        cont = connect.delperson(name,phone)
        for i in cont:
            print(f"{i['name']} : {i['phone']}")




