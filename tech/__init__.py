import asyncio
from pyrogram import Client
from pyromod import listen 
from tech import config

import pymysql
 
 
# establish connection to MySQL
connection = pymysql.connect(
    host="localhost",
    user="id21233481_khansa",
    password="Knsgnwn#1",
    port=3306,
    db="id21233481_zenblogger"
)
 
# make cursor for establish connection
mycursor = connection.cursor()
mycursor.execute("Select * from geeksdemo")
myresult = mycursor.fetchall()
for i in myresult:
    print(i)
     
     
# statement to insert record
mycursor.execute(
    "Insert into geeksdemo(id,name,gender,dept) \
    select * from( Select 5,'Thomas','m','information technology') as temp \
    where not exists \
    (Select id from geeksdemo where id=5) LIMIT 1")
print("After inserting a record....")
 
 
# print records after insertion
mycursor.execute("Select * from geeksdemo")
 
 
myresult = mycursor.fetchall()
for i in myresult:
    print(i)
mycursor.execute("Commit")
 
 
# close connection
connection.close()
manage = Client(
  name=":memory:",
  api_id=config.API_ID,
  api_hash=config.API_HASH,
  bot_token=config.BOT_TOKEN,
  plugins={"root": "tech.Manager"},
)
