import pymongo
clint = pymongo.MongoClient("https://github.com/DarshanShukla/MySQL_Exercise.git")

import mysql.connector

# establishing the connection
conn = mysql.connector.connect(
    user='root', password='Datascience#2023', host='localhost', database='darshan1'
)

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Dropping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS darshan1.AttributeDataset")

# Creating table as per requirement
sql = '''create table darshan1.AttributeDataset (Dress_ID BIGINT, Style varchar(500), Price varchar(500), Rating BIGINT,
    Size BIGINT, Season varchar(500), Neck_line varchar(500), Sleeve_Length varchar(500), Waise_Line varchar(500),
    Material varchar(500), fabric_type varchar(500), Decoration varchar(500), Pattern_type varchar(500), Recommendation BIGINT)'''

cursor.execute(sql)

# Closing the connection
conn.close()
