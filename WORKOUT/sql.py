
#show connection object
""" import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire")
print(connection) """


#create databases

""" import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire")
cursor=connection.cursor()
cursor.execute("create databases sandy07") """


#show all databases with in root user
""" import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire")
cursor=connection.cursor()
cursor.execute("show databases")
for x in cursor:
    print(x) """


#create tables
""" import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="sandy07")
cursor=connection.cursor()
cursor.execute("CREATE TABLE departments(department_id INT PRIMARY KEY,department_name VARCHAR(50))")
cursor.execute("show tables")
print ("Number of tables in database:")
for x in cursor:
    print("\t",x)
 """

""" import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="sandy07")
cursor=connection.cursor()
cursor.execute("CREATE TABLE employes(employee_id INT PRIMARY KEY,employee_name VARCHAR(100),department_id INT)")
cursor.execute("show tables")
print ("Number of tables in database:")
for x in cursor:
    print("\t",x)
 """

""" import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="sandy07")
cursor=connection.cursor()
s="insert into employes values (%s,%s,%s)"
t=(1,"mani",1)
cursor.execute(s,t)
connection.commit()
print(cursor.rowcount,"new row inserted") """


""" import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="sandy07")
cursor=connection.cursor()
s="insert into employes values(%s,%s,%S)"
t=[(2,"mani",1),(3,"mani",2)]
cursor.executemany(s,t)
connection.commit()
print(cursor.rowcount,"new row inserted") """


""" import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="livewire",database="sandy07")
cursor=connection.cursor()
cursor.execute("select * from employess")
result=cursor.fetchall()
print("content in the python:")
for x in result:
     print("\t",x) """


""" import pymysql as mysql 
connection=mysql.connect(host="localhost",user="root",password="livewire",database="sandy07")
cursor=connection.cursor()
sql="Update employees set employee_name='bala' Where employee_id=1;"
cursor.execute(sql)
connection.commit() """


import pymysql as mysql
connection=mysql.connect(host="localhost",user="root",password="sandy07")
cursor=connection .cursor()
sql="DELETE From employee WHERE employee_id=1 "
cursor.execute(sql)
connection.commit()
print (cursor.rowcount,"record(s) deleted")


