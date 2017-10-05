from flask import Flask, request, redirect, render_template
import cgi


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if username == '' or len(username) <= 3 or len(username) >= 20:
        username_error = "Please enter a valid username."
        username = ''
    
        
    if verify_password != password:
        verify_error = "Passwords do not match."
        verify_password = ''
        password = ''
    
    if password == '' or len(password) <=3 or len(password)>=20 :
        password_error = "Please enter a valid password."
        password = ''

    if (email != '' and "@" not in email) and (len(email) <=3 or len(email)>=20):
        email_error = "Please enter a valid email address."
        email = ''
    
    if not username_error and not password_error and not email_error and not verify_error:
        return render_template('success.html', username = username)
    else: 
        return render_template('edit.html', username_error = username_error, 
                                            password_error=password_error, 
                                            verify_error=verify_error, 
                                            email_error=email_error)


@app.route("/")
def index():
    return render_template('edit.html')


app.run()