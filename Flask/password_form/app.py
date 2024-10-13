from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

password = "password"

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    entered_password = request.form['password']
    if entered_password == password:
        return redirect(url_for('success'))
    else:
        return render_template('login.html', error='Wrong password, try again. 🙂')

@app.route('/success')
def success():
    return "Welcome rauf 😊"

if __name__ == '__main__':
    app.run(debug=True)
