import mysql.connector
mydb=mysql.connector.connect(
        host='localhost',
        user='root',
        password='I\'llmakeit',
        database='Omar_bank')

def create_acc():
    acc_num=input('Enter Account Number: ')
    pin=input('Enter your PIN: ')
    n=input('Enter Name: ')
    balance=int(input('Enter the opening balance: '))
    sql=(f"""INSERT INTO `Omar_bank`.`People` (`Acc_ID`,`PIN`,`Name`,`Balance`) VALUES ('{acc_num}','{pin}','{n}',{balance});""")
    x=mydb.cursor()
    x.execute(sql)
    mydb.commit()
    print('\nAccount succesfully created\n')
    menu()

def deposit():
    acc=input('Enter Account ID: ')
    amount=int(input('Enter the amount you want to deposit: '))
    a=(f"""UPDATE People SET Balance= Balance+{amount} WHERE Acc_ID={acc} ;""")
    x=mydb.cursor()
    x.execute(a)
    mydb.commit()
    print(f'\n{amount}$ succsesfully deposited\n')
    menu()

def withdraw():
    acc=input('Enter Account ID: ')
    amount=int(input('Enter the amount you want to withdraw: '))
    a=(f"""UPDATE People SET Balance= Balance-{amount} WHERE Acc_ID={acc} ;""")
    x=mydb.cursor()
    x.execute(a)
    mydb.commit()
    print(f'\n{amount}$ succesfully withdrew\n ')

    menu()
def check():
    acc=int(input('Enter acc #: '))
    a=f"""SELECT Balance FROM People WHERE Acc_ID={acc};"""
    data=(acc,)
    x=mydb.cursor()
    x.execute(a)
    result=x.fetchone()
    if result is None:
        print("No balance found for this acount")
    else:
        balance=result[0]
        print("Balance for account ID:",acc, "is",balance)
    mydb.close()
    menu()

def details():
    acc=input('Enter Account ID: ')
    a=(f"""SELECT * FROM People WHERE Acc_ID={acc};""")
    x=mydb.cursor()
    x.execute(a)
    result=x.fetchone()
    #for i in result:
       # print(i)
    if result is not None:
        print(f"{'Acc_ID'}    {'PIN'}    {'Name'}   {'Balance'}")
        print(f"{result[0]} {result[1]} {result[2]} {result[3]}")
    else:
        print('Account not found')
    x.close()
    mydb.close()
    menu()
def close_acc():
    acc=input('Enter Account ID: ')
    sql=f"""DELETE FROM People WHERE Acc_ID={acc};"""
    x=mydb.cursor()
    x.execute(sql)
    mydb.commit()
    print('\n','Account closed succesfully\n')
    menu()








def menu():
    print('-----Hello user-----')
    selection=int(input('Choose from the following options:\n1.Create an account\n2.Deposit\n3.Check Balance\n4.Withdraw\n5.Account details\n6.close account\n7.Exit '))
    if selection==1:
        create_acc()
    elif selection==2:
        deposit()
    elif selection==3:
        check()
    elif selection==4:
        withdraw()
    elif selection==5:
        details()
    elif selection==6:
        close_acc()
    elif selection==7:
        print('Have a Nice day!')
    else:
        print('Error')
        menu()


menu()