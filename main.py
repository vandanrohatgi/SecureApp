from flask import Flask, render_template, request,redirect,g,session,url_for
import os
from MongoDB import database
import re
from werkzeug.security import check_password_hash


app=Flask(__name__,static_url_path='',static_folder='web/static',template_folder='web/templates')
app.secret_key=os.urandom(12)
app.env="development"
app.debug=True

db=database()


@app.before_request
def before_request():
    g.user=None
    if 'user' in session:
        g.user=session['user']


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user', None)

        username = request.form.get('username')
        password = request.form.get('password')
        record=db.query(username)
        if record['username'] and check_password_hash(record['password'],password):
            session['user']=username
            return redirect(url_for('welcome'))
        return render_template('index.html',error="Username and/or password incorrect")
    return render_template('index.html')

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/welcome')
def welcome():
    if not g.user:
        return redirect(url_for('login'))
    return render_template('welcome.html',username=session['user'])

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for('login'))

@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))
    return render_template('profile.html',username=session['user'])

@app.route('/update',methods=['POST'])
def update():
    if not g.user:
        return redirect(url_for('login'))
    if request.method=='POST':
        action=request.form.get('action')
        
    else:
        return redirect(url_for('profile'))

# create method to check for special chars
#     
    

if __name__ == "__main__":
    app.run()