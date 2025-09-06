import mysql.connector as a

con-a.connect(host="localhost", user="root",passwd="123456")

C=con.cursor()

sql1= "create database jail"

c.execute(sql1)

sql2="use jail"

c.execute(sq12)

sq13="create table prisoners (P_ID varchar(7) Primary Key, P_nane varchar(9), CRIME varchar(10), AGE INTEGER(8), P_DURATION decimal(10))"

c.execute(sq13)

con.commit()

print("connection established")

import mysql.connector as a

def connect_to_database():
    con =a.connect(host="localhost", user="root", passwd="123456", database="JAIL")
    return con

def add_new_prisoner(con):
    n= input("Enter P_ID: ")
    C=input("Enter P_NAME: ")
    r=input("Enter CRIME: ")
    b=int(input("Enter AGE: "))
    p=float(input("Enter P_DURATION: "))
    data (n, c, r, b, p)
    sql='INSERT INTO PRISONERS VALUES (%s, %s, %s, %s, As)'
    with con.cursor() as cursor:
        cursor.execute(sql, data)
        con.commit()
        print("Data Entered Successfully")

def display_prisoners(con):
    sql="SELECT FROM PRISONERS"
    with con.cursor() as cursor:
        cursor.execute(sql)
        d=cursor.fetchall()
        for i in d:
            print(i)


elif n == '3':

ct = input("Enter CRIME: ")

sql = "SELECT * FROM PRISONERS WHERE CRIME = %s"

with con.cursor() as cursor:
    cursor.execute(sql, (ct,))

d = cursor.fetchall()

for i in d:
    print(i)

def sort_prisoners(con):
    print("Choose option for sorting:")
    print("1. AGE")
    n = input("Press your Choice: ")
    if n == '1':
        sql = "SELECT FROM PRISONERS ORDER BY AGE"
    with con.cursor() as cursor:
        cursor.execute(sql)
        d = cursor.fetchall()
        for i in d:
            print(i)

def delete_prisoner(con):
    print("Choose option for deletion:")
    print("1. PRISONER NAME")
    print("2. PRISONER ID")
    print("3. CRIME AND PRISONER NAME")
    n = input("Press your Choice: ")

    if n == '1':
        nm= input("Enter PRISONER NAME: ")
        sql = "DELETE FROM PRISONERS WHERE P_name = %s"
        with con.cursor() as cursor:
            cursor.execute(sql, (nm,))
            print("Record deleted successfully")
    elif n== '2':
        pn=input("Enter PRISONER ID: ")
        sql = "DELETE FROM PRISONERS WHERE P_ID = %s"
        with con.cursor() as cursor:
            cursor.execute(sql, (pn,)) 
            print("Record deleted successfully")

    elif n== '3':
        ct=input("Enter CRIME: ")
        nm= input("Enter PRISONER NAME: ")
        sql="DELETE FROM PRISONERS WHERE CRIME = %5 AND P NAME=%s"
        with con.cursor() as cursor:
            cursor.execute(sql, (ct, nm))
            print("Record deleted successfully")

def update_prisoner(con):

    p_id= input("Enter the P_ID of the prisoner you want to update: ")
    print("Select the detail to update:")
    print("1. P_NAME")
    print("2. P_DURATION")
    choice = input("Enter your choice: ")

    if choice == '1':
        new_name = input("Enter the new P_NAME: ")
        sql = "UPDATE PRISONERS SET P_NAME=%s WHERE P_ID = %s"
        data = (new_name, p_id)


    elif choice=='2':
        new_duration = float(input("Enter the new P_DURATION: "))
        sql="UPDATE PRISONERS SET P DURATION = %s WHERE PID = %s"
        data (new_duration, p_id)
    else:
        print("Invalid choice")
        return

    with con.cursor() as cursor:
        cursor.execute(sql, data)

    con.commit()
    print("Data Updated Successfully")

def main():
    while True:
        print("********************************")
        print("1. ADO NEW PRISONER'S INFORMATION")
        print("2. DISPLAY PRISONERS INFORMATION IN OUR DATABASE")
        print("3. SEARCH PRISONER INFORMATION")
        print("4. SORT PRISONER INFORMATION")
        print("5. DELETE A PARTICULAR PRISONER RECORD")
        print("6. UPDATE A PRISONER RECORD")
        print("7. QUIT")
        print("................................")

        choice=input("Enter Task No: ")

        if choice =='1':
            add_new_prisoner(con)

        elif choice =='2':
            display_prisoners(con)

        elif choice=='3':
            search_prisoner(con)

        elif choice =='4':
            sort_prisoners(con)

        elif choice == '5':
            delete_prisoner(con)

        elif choice =='6':
            update_prisoner(con)
        elif choice =='7':
            con.close()
            exit()
        else:
            print("Wrong choice")

if name=="main":

    main()