from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current


app = Flask(__name__)

import os
print(os.getcwd())
print(app.jinja_loader.searchpath)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if  username == 'Admin' and password == 'password':
            return 'Login Successfull'
        else:
            return 'Invalid Credentials'
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run()