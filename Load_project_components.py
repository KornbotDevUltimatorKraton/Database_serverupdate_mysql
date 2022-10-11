import json 
import requests
import threading
import mysql.connector
from flask import Flask,render_template,url_for,jsonify,request
app = Flask(__name__) 
Database="Configure_components"
mydb = mysql.connector.connect(
  host="localhost",
  user="roboreactorclassifier",
  password="roboreactorclassifier",
  database=Database
)
New_data_json = {}  # Getting the new data  to check if not exist then add the new one inside the json 
mycursor=mydb.cursor()

query="SELECT*FROM "+Database
#query = "SELECT COUNT(1) FROM Components_project WHERE email = 'kornbot380@hotmail.com'"
mycursor.execute(query) 
rows=mycursor.fetchall()
print(rows)
if rows !=[]:
     for row in rows:
            New_data_json[row[0]] = json.loads(row[1])

@app.route("/",methods=['POST'])
def index():
   inputjson = request.get_json(force=True) # Getting the post request from the web database postrequest 
   print(inputjson)
   email_data = list(inputjson)[0] 
   value_data = json.dumps(inputjson.get(list(inputjson)[0])) 
   query = "SELECT COUNT(1) FROM "+Database+" WHERE email = '"+email_data+"'"
   mycursor.execute(query) 
   rows=mycursor.fetchall()
   print(rows)
  
   if rows == [(0,)]:
      #mycursor = mydb.cursor()
      sql = "INSERT INTO "+Database+" (email, load_project_components) VALUES (%s, %s)"
      val = (email_data,value_data) # Getting the value from json  
      mycursor.execute(sql, val)
      mydb.commit()     
      print(mycursor.rowcount, "record inserted.")
      New_data_json [email_data] = json.loads(value_data)
   if rows == [(1,)]:
       # Add all the data inside the json  
       print("The data is already exist")
       sql = "UPDATE "+Database+" SET load_project_components  ='"+value_data+"'"
       mycursor.execute(sql)
       mydb.commit()
       print(mycursor.rowcount, "updated_record(s) affected")
       New_data_json [email_data] = json.loads(value_data) 
   return jsonify(inputjson)
@app.route("/api_data")
def api_data():
   
      return jsonify(New_data_json)
if __name__=="__main__":

        app.run(debug=True,threaded=True,host="0.0.0.0",port=8001)
