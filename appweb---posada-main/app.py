from flask import Flask
from flask import render_template, request, redirect, session
from flaskext.mysql import MySQL
from datetime import datetime
from flask import send_from_directory
import os
import hashlib
from admin import Administrador
from categorias import Categorias


app = Flask(__name__)
app.secret_key = "digitalforge"

mysql = MySQL()

app.config['MYSQL_DATABASE_HOST']='10.206.66.185'
app.config['MYSQL_DATABASE_USER']='backend_2'
app.config['MYSQL_DATABASE_PASSWORD']='@Andres4321'
app.config['MYSQL_DATABASE_DB']='visitabuga'
mysql.init_app(app)

conexion = mysql.connect()
cursor = conexion.cursor()

losOperadores = Administrador(mysql)
lasCategorias = Categorias(mysql)


@app.route('/')
def admin_index():
    return render_template('admin/index.html')

@app.route('/admin/login')
def adminLogin():
    return render_template('admin/login.html')

@app.route('/admin/verAdmin')
def verAdmin():

    resultados = losOperadores.consultarAdmin()

    return render_template("admin/verAdmin.html", admins = resultados)

@app.route('/admin/agregar', methods = ['POST'])
def agregarAdmin():
    nombre = request.form['txtNombre']
    apellido = request.form['txtApellido']
    cedula = request.form['txtCedula']
    correo = request.form['txtCorreo']
    celular = request.form['txtCelular']
    contrasena = request.form['txtPassword']

    cifrada = hashlib.sha512(contrasena.encode("utf-8")).hexdigest()

    rol = 'ad'

    estado = 'activo'

    if not losOperadores.buscarAdmin(correo):

        user_registro = "usuario_que_realiza_el_registro"

        losOperadores.agregarAdmin([nombre, apellido, cedula, correo, celular, rol, cifrada, estado], user_registro)
    
    else: 

        return render_template('admin/verAdmin.html' , men = "Correo no disponible")

    return redirect('/admin/verAdmin')



@app.route('/admin/categ')
def admincateg():

    resultado_categorias = lasCategorias.consulta_categorias()
    
    return render_template('admin/categorias.html', admin_cate = resultado_categorias)





@app.route('/admin/categ/agregar', methods= ['POST'])
def agregarCategoria():

    nombre_categorias = request.form['txtCategorias']

    user_registro = "usuario_que_realiza_el_registro"

    lasCategorias.agregar_categorias([nombre_categorias], user_registro)

    return redirect('/admin/categ')




if __name__ == '__main__':
    app.run(debug=True)