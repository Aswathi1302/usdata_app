import requests
import json
import sys
import mysql.connector
try:
   mydb=mysql.connector.connect(host='localhost',user='root',password='',database='usdatadb')
except mysql.connector.Error as e:
    sys.exit("db connection error",e)    
mycursor = mydb.cursor()  


data=requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population").text
data_info=json.loads(data)
print(data_info)
data1= data_info["data"]
for i in data1:
    ID_Nation = str(i['ID Nation'])
    Id_Year=str(i['ID Year'])
    Year=str(i['Year'])
    Population=str(i['Population'])
    sql="INSERT INTO `usdata`(`ID_Nation`, `Nation`, `ID Year`, `Year`, `Population`, `Slug Nation`) VALUES ('"+ID_Nation+"','"+i['Nation']+"','"+Id_Year+"','"+Year+"','"+Population+"','"+i['Slug Nation']+"')"
    mycursor.execute(sql)
    mydb.commit()
    print("Data inserted successfully", i['ID Nation'])