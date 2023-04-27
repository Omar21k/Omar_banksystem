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
    balance=input('Enter the opening balance: ')
    sql1=("""INSERT INTO `Omar_bank`.`People` (`Acc_ID`,`PIN`,`Name`,`Balance`) VALUES ('{acc_num}','{pin}','{n}',{balance})""")
    x=mydb.cursor()
    x.execute(sql1)
    mydb.commit()
    print('Data succesfully added')
    menu()
def deposit():
    acc=('Enter account number: ')
    amount=('Enter the amount you want to deposit: ')
    menu()

#def withdraw():
    amount=('Enter the amount you want to withdraw: ')
    acc=('Enter account number: ')
    a='select Balance from Clients1 where Acc_ID=%s'
    data=(acc,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[0]-amount
    sql='update Clients1 set Balance where Acc_ID=%s'
    d=(t,acc)
    x.execute(sql,d)
    mydb.commit()
    menu()
#def check():
    acc=int(input('Enter acc #: '))
    a='select from * Clients1 where Acc_ID=%s'
    data=(acc,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    print('Balance for account:',acc,'is',result[-1])
    menu()

#def details():
    acc=int(input('Enter acc #: '))
    a='select from * Clients1 where Acc_ID=%s'
    data=(acc,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    for i in result:
        print(i)
    menu()
#def close_acc():
    acc=int(input('Enter Acc_ID: '))
    sql1='delete from Clients1 where Acc_ID=%s'
    data=(acc,)
    x=mydb.cursor()
    x.execute(sql1)
    mydb.commit()
    menu()








def menu():
    print('-----Hello user-----')
    selection=int(input('Choose from the following options:\n1.Create an account\n2.Deposit\n3.Check Balance\n4.Withdraw\n5.Account details\n6.close account '))
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
    else:
        print('Error')
        menu()
menu()