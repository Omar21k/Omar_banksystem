import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='I\'llmakeit',
        database='Omar_bank'

    )
if __name__=='__main__':
    conection=connect_to_db()
    print(conection)
    cursor=conection.cursor()
    cursor.execute("Select * FROM People")
    for x in cursor.fetchall():
        print(x)