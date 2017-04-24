#import pandas as pd
#import datetime
import os
import mysql.connector
import json
import shutil

def IV_textreader(filename):
    file = open(filename,'r')
    chipId = file.readline().strip()
    Date = file.readline().strip()
    comment = file.readline().strip()
    
    return chipId, Date, comment

def create_connection():
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = mysql.connector.connect(user='user', password='password',
                              host='IP address',
                              database='new_schema')
        return conn
    except mysql.connector.Error as e:
        print(e)

    return None

def insert_IV_record(conn, chipId, Date, comment, IVdatalist):
   
    add_recipe = ("INSERT INTO NEA_iv "
                    "(Date, chipId, CH1, CH2, CH3, CH4, CH5, CH6, CH7, CH8, CH9, CH10, CH11, CH12, CH13, CH14, CH15, CH16, CH17, CH18, CH19, CH20, CH21, CH22, comment) "
                     "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s)")
    
    data_recipe = (Date,chipId,IVdatalist[0],IVdatalist[1],IVdatalist[2],IVdatalist[3],IVdatalist[4],IVdatalist[5],IVdatalist[6],IVdatalist[7],IVdatalist[8],IVdatalist[9],IVdatalist[10],IVdatalist[11],IVdatalist[12],IVdatalist[13],IVdatalist[14],IVdatalist[15],IVdatalist[16],IVdatalist[17],IVdatalist[18],IVdatalist[19],IVdatalist[20],IVdatalist[21],comment)
    
    try:
        c = conn.cursor()
        c.execute(add_recipe,data_recipe)
        conn.commit()
    except mysql.connector.Error as e:
        print (e)
        print(" *** Warn: Could not insert recipe record in database ", chipId)





#PATHS
temp = 'C:/Users/labuser/Documents/NEA_Scripts/Final_Scripts/IV_Temp/'
os.chdir(temp)

#Iterate throught the folders
folderlist = os.listdir()

for folder in folderlist:
    #Go to the folder
    os.chdir(temp+folder+'/')
    
    #List text files
    textfile = [i for i in os.listdir() if '.txt' in i][0]
    
    #List json files
    jsonlist = [i for i in os.listdir() if '.txt' not in i]
    
    #Collect data in the variables
    
    chipId, Date, comment = IV_textreader(textfile)
    #print (chipId)
    #print(Date)
    
    IVdatalist = []
    for jsonn in jsonlist:
        with open(jsonn) as json_data:
            d = json.load(json_data)
            d = json.dumps(d)
        IVdatalist.append(d)
        
    
    #Put the data in the database
    conn = create_connection()
    insert_IV_record(conn, chipId, Date, comment, IVdatalist)
    
    os.chdir(temp)
    shutil.rmtree(temp+folder)
    
    