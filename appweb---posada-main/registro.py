

from flask import Flask, render_template, request
from flaskext.mysql import MySQL
import mysql.connector
import hashlib
import conexion


app = Flask (__name__)
# Ruta para el formulario de registro
@app.route('/')
def principal():
    return render_template('registro.html')

@app.route('/registro', methods=[ 'POST'])
def registro():
    if request.method == 'POST':
            nombres = request.form["nombre"]
            apellidos = request.form["apellido"]
            cedula = request.form["cedula"]
            correo = request.form["correo"]
            foto = request.files["foto"]
            celular = request.form["celular"]
            clave = request.form["clave"]
            cifrada = hashlib.sha512(clave.encode("utf-8")).hexdigest()
            
            
            # print(f"INSERT INTO turistas (nombres, apellido, cedula, correo, foto, celular, clave) VALUES ('{nombres}', '{apellidos}', '{cedula}', '{correo}', '{foto}', '{celular}', '{cifrada}'))")
            
            
            sql = ("INSERT INTO `turistas` (nombres, apellido, cedula, correo, foto, celular, clave) VALUES (%s, %s, %s, %s, %s, %s, %s)")
            datos = (nombres, apellidos, cedula, correo, foto, celular, cifrada)
            cone = mysql.connect()
            cursor = cone.cursor()
            cursor.execute(sql,datos)
            cone.commit()

            cone.close()

            

            return render_template('loginTuristas.html')
            print("error insercion sql")

    else:
        print("error de peticion post")# return render_template('loginTuristas.html')  # Mostrar formulario de registro

if __name__ == '__main__':
    app.run(debug=True)