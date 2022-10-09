import threading
import mysql.connector
from flask import Flask,render_template,url_for,jsonify,request
app = Flask(__name__) 
url = "https://roboreactor.com/components_project_data" # Getting the component project list to insert into the system 
mydb = mysql.connector.connect(
  host="localhost",
  user="roboreactorclassifier",
  password="roboreactorclassifier",
  database="Components_project"
)

New_data_json = {}  # Getting the new data  to check if not exist then add the new one inside the json 
mycursor=mydb.cursor()

@app.route("/",methods=['POST'])
def index():
   inputjson = request.get_json(force=True) # Getting the post request from the web database postrequest 
   print(inputjson)
   email_data = list(inputjson)[0] 
   value_data = json.dumps(inputjson.get(list(inputjson)[0])) 
   query = "SELECT COUNT(1) FROM Components_project WHERE email = '"+email_data+"'"
   mycursor.execute(query) 
   rows=mycursor.fetchall()
   print(rows)
  
   if rows == [(0,)]:
      #mycursor = mydb.cursor()
      sql = "INSERT INTO Components_project (email, Components_project) VALUES (%s, %s)"
      val = (email_data,value_data) # Getting the value from json  
      mycursor.execute(sql, val)
      mydb.commit()     
      print(mycursor.rowcount, "record inserted.")

   if rows == [(1,)]:
       # Add all the data inside the json  
       print("The data is already exist")
       sql = "UPDATE Components_project SET Components_project='"+value_data+"'"
       mycursor.execute(sql)
       mydb.commit()
       print(mycursor.rowcount, "updated_record(s) affected")
   return jsonify(inputjson)

if __name__=="__main__":
          app.run(debug=True,threaded=True,host="0.0.0.0",port=8000)
  
