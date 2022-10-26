import mysql.connector as darshan

mydb = darshan.connect(host="localhost", user="root", passwd="Datascience#2023")
# print(mydb)
cursor = mydb.cursor()
cursor.execute("show databases")
print(cursor.fetchall())

mycursor = mydb.cursor()
cursor.execute("DROP TABLE IF EXISTS darshan1.AttributeDataset")
sql_query = '''create table darshan1.AttributeDataset (Dress_ID BIGINT, Style varchar(500), Price varchar(500), Rating BIGINT,
    Size BIGINT, Season varchar(500), Neck_line varchar(500), Sleeve_Length varchar(500), Waise_Line varchar(500),
    Material varchar(500), fabric_type varchar(500), Decoration varchar(500), Pattern_type varchar(500), Recommendation BIGINT)'''

mycursor.execute(sql_query)
mydb.commit()
mydb.close()