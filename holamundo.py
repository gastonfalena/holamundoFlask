from flask import Flask,request,url_for,redirect,abort,render_template

app =  Flask(__name__)

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