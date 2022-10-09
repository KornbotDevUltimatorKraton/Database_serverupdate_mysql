import json 
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="roboreactorclassifier",
  password="roboreactorclassifier",
  database="Components_project"
)

mycursor = mydb.cursor()
value = json.dumps({'kornbot380@hotmail.com': {'Roboreactor_devian_8': {'Vision_system': [{'Fish_eye_lens_camera': '8MPX', 'rpiCamera': '5MPX'}], 'Navigation_system': [{'Intel_Realsense_RPLIDAR_A2': 'Serial', 'QUECTEL_EC25_v3': 'UART'}], 'Motion_system': [{'RoboticsJoint3': 'Serial'}]}}})
#sql = "UPDATE Components_project SET email = 'kornbot380@hotmail.com' WHERE Components_project = '"+value+"'"
sql = "UPDATE Components_project SET Components_project='"+value+"'"
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

