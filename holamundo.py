from flask import Flask,request,url_for,redirect,abort,render_template
from decouple import config
import mysql.connector

app =  Flask(__name__)

MYSQL_HOST , MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB = config('MYSQL_HOST'),config('MYSQL_USER'), \
config('MYSQL_PASSWORD'),config('MYSQL_DB')

midb = mysql.connector.connect(
   host = MYSQL_HOST,
   user = MYSQL_USER,
   password = MYSQL_PASSWORD,
   database = MYSQL_DB
)
cursor = midb.cursor(dictionary=True)

@app.route('/')
def index():
    return 'hola mundo'

@app.route('/get/<get_id>',methods=['GET'])
def getId(get_id):
    return 'el id del post es:%s' % get_id

@app.route('/post/<post_id>',methods=['POST'])
def postId(post_id):
    return 'el id del post es:%s' % post_id

@app.route('/form',methods=['POST'])
def form():
    print(url_for('getId',get_id=2))
    print(request.form)
    print(request.form['llave1'])
    return 'hola mundo'
@app.route('/redirect',methods=['POST','GET'])
def redirect1():
    return redirect(url_for('getId',get_id=2))
   
@app.route('/render',methods=['POST','GET'])
def render():
    return render_template('hola.html')
@app.route('/json',methods=['POST','GET'])
def json():
    return{
        "username":"fale",
        "email":"fale@outlook.com"
    }

@app.route('/home',methods=['GET'])
def home():
    return render_template('home.html',mensaje='Hola Mundo')

@app.route('/db',methods=['GET'])
def db():
    cursor.execute('select * from Usuario')
    usuarios = cursor.fetchall()
    return  render_template('hola.html',usuarios=usuarios)


@app.route('/crear',methods=['GET','POST'])
def crear():
    if request.method=="POST":
        username = request.form['username']
        email = request.form['email']
        sql="insert into Usuario(username,email) values(%s,%s)"
        #utilizamos value para que en username no puedan hacer sql injection
        values=(username,email) 
        #la funcion se encarga de concatenar los nombres correctamente
        cursor.execute(sql,values)
        midb.commit()
        return redirect(url_for('db'))
    return render_template('crear.html') 