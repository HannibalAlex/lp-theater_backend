# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

try:
    conn = mysql.connector.connect(
    host="HannibalAlex.mysql.pythonanywhere-services.com",
    user="HannibalAlex",
    password="&b]st:Z8%R9d3XCPN<1?@Yt",
    database="HannibalAlex$teatro_lp"
    )
    mensaje = 'Grupo 2, Com. 24187, conectado :)'
    mycursor = conn.cursor()

except mysql.connector.Error as e:
    results = ["#"]
    mensaje = '¡NO ESTÁS CONECTADO!'

def add_character(Nombre, Apellido, Documento, Email, Password):
    query = "INSERT INTO teatro_arg (Nombre, Apellido, Documento, Email, Password) VALUES (%s, %s, %s, %s, %s);"
    values = (Nombre, Apellido, Documento, Email, Password)
    mycursor.execute(query, values)
    conn.commit()

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        Nombre = request.form['Nombre']
        Apellido = request.form['Apellido']
        Documento = request.form['Documento']
        Email = request.form['Email']
        Password = request.form['Password']
        add_character(Nombre, Apellido, Documento, Email, Password)
    mycursor.execute("SELECT * FROM teatro_arg")
    results = mycursor.fetchall()
    return render_template('index.html', mensaje = mensaje, results = results)