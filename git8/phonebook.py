from connect import connecting

conn = connecting()
cur = conn.cursor()

ist = True
while(ist):
    inp = input()
    if inp == "1":
        pinp = input()
        cur.execute("SELECT * FROM SEARCH_NAME(%s)", (pinp,))
        print(cur.fetchall())
    if inp == "2":
        pinp = input()
        cur.execute("SELECT * FROM SEARCH_NUMBER(%s)", (pinp,))
        print(cur.fetchall())
    if inp == "3":
        inp_name = input()
        inp_number = input()
        cur.execute("CALL UPSET_USER(%s,%s)",(inp_name,inp_number))
        print('good!')
        conn.commit()
    if inp == "4":
        inp_oname = input()
        inp_onumber = input()
        inp_name = input()
        cur.execute("CALL UPDATE_NAME(%s,%s,%s)",(inp_onumber,inp_oname,inp_name))
        print('good!')
        conn.commit()
    if inp == "5":
        inp_dname = input()
        inp_dnumber = input()
        cur.execute("CALL DELETE_COL(%s,%s)",(inp_dname,inp_dnumber))
        print('good!')
        conn.commit()
    if inp =="6":
        print('poka!\n')
        print('final result: ')
        ist = False

cur.execute("SELECT * FROM phonebook;")
print(cur.fetchall())

conn.close()