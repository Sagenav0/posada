import mysql.connector

back = mysql.connector.connect(user='backend_1', password='@Nico1234',host='10.206.66.185',database='visitabuga',port='3306')

back_conexion = back.cursor()

back_conexion.execute("SELECT nombres,rol* FROM operadores ")

resultado = back_conexion.fetchall()

print (resultado)

