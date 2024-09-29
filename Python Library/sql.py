
#show connection object
""" import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire")
print(connection)
 """

#create database
""" import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire")
cursor=connection.cursor()
cursor.execute("Create database goodsanthosh97")
 """

#show all database with in root user 
""" import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire")
cursor=connection.cursor()
cursor.execute("show databases")
for x in cursor:
    print(x) """

#create table
""" import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="goodsanthosh97")
cursor=connection.cursor()
cursor.execute("CREATE TABLE departments(department_id INT PRIMARY KEY,department_name VARCHAR(50))")
cursor.execute("show tables")
print("Number of tables in database:")
for x in cursor:
    print("\t",x)  """

""" import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="goodsanthosh97")
cursor=connection.cursor()
cursor.execute("CREATE TABLE employes(employee_id INT PRIMARY KEY,employee_name VARCHAR(100),department_id INT)")
cursor.execute("show tables")
print("Number of tables in database:")
for x in cursor:
    print("\t",x)"""
    


import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="goodsanthosh97")
cursor=connection.cursor()
s="insert into employee values(%s,%s,%s)"
t=(1,"sandy",1)
cursor.execute(s,t)
connection.commit()
print(cursor.rowcount,"new row inserted")
