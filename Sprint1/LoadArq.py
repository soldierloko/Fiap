import pandas as pd
import pyodbc

server = 'DESKTOP-2CHH2HH\SQLEXPRESS' 
database = 'IAG' 
username = 'myusername' 
password = 'mypassword' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
