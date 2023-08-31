from tabulate import tabulate
import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="jovi1504",database="Crud_data")


def insert(name, age, city):
    res = con.cursor()
    sql = "insert into users (name,age,city) values (%s,%s,%s)"
    user = (name, age, city)
    res.execute(sql, user)
    con.commit()
    print("Data Insert Success")
def update(name, age, city,id):
    res = con.cursor()
    sql = "update users set name=%s,age=%s,city=%s where id=%s"
    user = (name, age, city,id)
    res.execute(sql, user)
    con.commit()
    print("Data Update Success")



def select():
    res=con.cursor()
    sql="SELECT ID,NAME,AGE,CITY FROM USERS"
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=["ID""NAME","AGE","CITY"]))

def delete(id):
    res = con.cursor()
    sql = "delete from users where id=%s"
    user = (id,)
    res.execute(sql, user)
    con.commit()
    print("Data Delete Success")
def Exit():
    pass

while True:
    print("1.Insert Data")
    print("2.Update Data")
    print("3.Select Data")
    print("4.Delete Data")
    print("5.Exit.")
    choice=int(input("Enter your choice: "))
    if choice==1:
        name=input("Enter your Name: ")
        Age = input("Enter your Age: ")
        city = input("Enter your City: ")
        insert(name,Age,city)
    elif choice == 2:
            id=input("Enter The Id: ")
            name = input("Enter your Name: ")
            Age = input("Enter your Age: ")
            city = (input("Enter your City: "))
            update(name,Age,city,id)
    elif choice ==3:
        select()
    elif choice==4:
        id=input("Enter the Id to delete: ")
        delete(id)
    elif choice ==5:
        Exit()
        print("Thank you")
        break

    else:
        print("invalid user!.please try again")



