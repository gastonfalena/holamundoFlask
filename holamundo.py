from flask import Flask

app =  Flask(__name__)

@app.route('/')
def index():
    return 'hola mundo'

@app.route('/post/<post_id>')
def lala(post_id):
    return 'el id del post es:%s' % post_id
