from flask import Flask  #Importamos el Framework
from flask import render_template,request,redirect, send_from_directory, url_for, flash
from flaskext.mysql import MySQL
from datetime import datetime  # Nos permitirá darle el nombre a la foto
import os

app = Flask(__name__)
app.secret_key = "CodoACodo"
mysql = MySQL()  #Estamos creando el objeto
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_PORT'] = 3307
app.config['MYSQL_DATABASE_DB'] = 'crudejemplo'
mysql.init_app(app)

CARPETA = os.path.join('uploads') #Referenccia a la carpeta Uploads
app.config['CARPETA'] = CARPETA #Indicamos que vamos a guardar esta ruta de la carpeta.


@app.route('/')
def index():
    sql = "SELECT * FROM `crudejemplo`.`personal`;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql) 
    personal = cursor.fetchall()
    conn.commit()
    return render_template('personal/index.html', personal=personal)

@app.route('/create')
def create():
    return render_template('personal/create.html')


@app.route('/store', methods=['POST'])
def storage():
    nombre = request.form['txtNombre']
    correo = request.form['txtCorreo']
    foto = request.files['txtFoto']

    if nombre == '' or correo == '' or foto.filename == '':
        flash('Debes completar todos los campos !!!')
        return redirect(url_for('create'))
        
    now = datetime.now() #Fecha y Hora de subida del archivo.
    tiempo = now.strftime("%Y%H%M%S")
    if foto.filename != '':
        nuevoNombreFoto = tiempo + foto.filename
        foto.save("uploads/" + nuevoNombreFoto)
    sql = "INSERT INTO `crudejemplo`.`personal` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, %s, %s, %s);"
    datos = (nombre, correo, nuevoNombreFoto)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    return redirect('/')

'''
@app.route('/store', methods=['POST'])
def storage():
    nombre = request.form['txtNombre']
    correo = request.form['txtCorreo']
    foto = request.files['txtFoto']

    if nombre == '' or correo == '' or foto.filename == '' :
        flash('Recuerda llenar todos datos de los campos')
        return redirect(url_for('create'))
    
    now = datetime.now() 
    tiempo = now.strftime("%Y%H%M%S")

    if foto.filename != '':
        nuevoNombreFoto = tiempo + foto.filename
        foto.save("uploads/" + nuevoNombreFoto)

    sql = f'INSERT INTO `crudejemplo`.`personal` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, "{nombre}", "{correo}", "{nuevoNombreFoto}");'
    
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute(sql)
    conn.commit()
    return redirect('/')
'''

@app.route('/destroy/<int:id>')
def destroy(id):
    sql = "DELETE FROM `crudejemplo`.`personal` WHERE id=%s;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT foto FROM `crudejemplo`.`personal` WHERE id=%s", id)
    fila = cursor.fetchall()
    os.remove(os.path.join(app.config['CARPETA'], fila [0][0]))
    cursor.execute(sql, id)
    conn.commit()
    return redirect('/')
'''
@app.route('/destroy/<int:id>')
def destroy(id):
    sql = f'DELETE FROM `crudejemplo`.`personal` WHERE id={id};'
    conn = mysql.connect()
    cursor = conn.cursor()
    sql_foto = f'SELECT foto FROM `crudejemplo`.`personal` WHERE id={id};'
    cursor.execute(sql_foto)
    fila = cursor.fetchall()
    os.remove(os.path.join(CARPETA, fila [0][0]))
    cursor.execute(sql)
    conn.commit()
    return redirect('/')
'''
@app.route('/edit/<int:id>')
def edit(id):
    sql = "SELECT * FROM `crudejemplo`.`personal` WHERE id=%s;"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, id)
    personal = cursor.fetchone()
    conn.commit()
    return render_template('personal/edit.html', personal=personal)

'''
@app.route('/edit/<int:id>')
def edit(id):
    sql = f'SELECT * FROM `crudejemplo`.`personal` WHERE id={id};'
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    personal = cursor.fetchall()
    conn.commit()
    return render_template('personal/edit.html', personal=personal)
'''

@app.route('/update', methods=['POST'])
def update():
    nombre = request.form['txtNombre']
    correo = request.form['txtCorreo']
    foto = request.files['txtFoto']
    id = request.form['txtID']
    # sql = "UPDATE `crudejemplo`.`personal` SET `nombre`=%s, `correo`=%s WHERE id=%s;" #Si no usamos f-string colocamos este codigo.

    # Acá utilizamos f-string en lugar del ejemplo de la actividad. (Ver 2º video en sección 1:06hs)
    sql = f'UPDATE `crudejemplo`.`personal` SET `nombre`="{nombre}", `correo`="{correo}" WHERE id={id};'
    # datos = (nombre, correo, id)
    conn = mysql.connect()
    cursor = conn.cursor()
    now = datetime.now()  # Fecha y Hora de subida del archivo.
    tiempo = now.strftime("%Y%H%M%S")

    if foto.filename != '':
        nuevoNombreFoto = tiempo + foto.filename
        foto.save("uploads/" + nuevoNombreFoto)
        cursor.execute("SELECT foto FROM `crudejemplo`.`personal` WHERE id=%s;", id)
        fila = cursor.fetchall()
        os.remove(os.path.join(app.config['CARPETA'], fila [0][0]))
        cursor.execute("UPDATE `crudejemplo`.`personal` SET foto=%s WHERE id=%s;", (nuevoNombreFoto, id))
        conn.commit()
    cursor.execute(sql) #Utilizamos de esta manera para usar f-string.
    # cursor.execute(sql, datos) #Si no usamos f-string colocamos este codigo.
    conn.commit()
    return redirect('/')

#Este código lo paso el profesor. Utilizamos f-string en remplazo de las tuplas.
#Video 3 sección 17 minutos.
'''
if foto.filename != '':
        nuevoNombreFoto = tiempo + foto.filename
        foto.save("uploads/" + nuevoNombreFoto)
        sql_foto = f'SELECT foto FROM `crudejemplo`.`personal` WHERE id={id};'
        cursor.execute(sql_foto)
        fila = cursor.fetchall()
        os.remove(os.path.join(CARPETA, fila [0][0]))
        sql_act_foto = f'UPDATE `crudejemplo`.`personal` SET foto="{nuevoNombreFoto}" WHERE id={id};'
        cursor.execute(sql_act_foto)
        conn.commit()
    cursor.execute(sql)
    conn.commit()
    return redirect('/')
'''
    
@app.route('/uploads/<nombreFoto>')
def uploads(nombreFoto):
    return send_from_directory(CARPETA, nombreFoto)


'''
@app.route('/uploads/<nombreFoto>')
def uploads(nombreFoto):
    return send_from_directory(app.config['CARPETA'], nombreFoto)
'''


if __name__ == '__main__':
    app.run(debug=True)
