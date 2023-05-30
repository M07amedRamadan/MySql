#!/bin/python3.9
import mysql.connector
connection=mysql.connector.connect (host="localhost",user="root",)
cursor=connection.cursor()

#create Database
print("Creating Database with 3 Columns.")
dbName=input("Enter name of DataBase: \n")
cursor.execute(f"CREATE DATABASE {dbName}")
#create Table
tableName=input("Enter table name: \n")
#create columns with datatypes.
column1= input("Enter first column Name : \n ")
datatype1=input(f"Enter datatype of {column1}:\n").upper()
column2= input("Enter second column  Name: \n ")
datatype2=input(f"Enter datatype of {column2}:\n").upper()
column3= input("Enter third column  Name : \n ")
datatype3=input(f"Enter datatype of {column3}:\n").upper()
cursor.execute(f"USE {dbName}")
cursor.execute(f"CREATE TABLE {tableName} ( {column1} {datatype1} ,{column2} {datatype2}, {column3} {datatype3}) ")
#enter values
value1=input(f"Enter value in {column1}: \n")
value2=input(f"Enter value in {column2}: \n")
value3=input(f"Enter value in {column3}: \n")
#cursor.execute(f"SHOW FULL TABLES")
cursor.execute(f"INSERT INTO {tableName} ({column1} ,{column2}, {column3}) VALUES ({value1}, {value2},{value3}) ")
print(" Data inserted into table.")
print("###########################")
print("Featching data from table.")
cursor.execute(f"SELECT * From {dbName}.{tableName}")
row =cursor.fetchall()
for record in row:
        print(record)

connection.commit()
connection.close()
