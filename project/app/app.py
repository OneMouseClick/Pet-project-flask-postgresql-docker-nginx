from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile("config.py")

conn = SQLAlchemy()
conn.init_app(app)

current_users = -1


class User(conn.Model):
    id = conn.Column(conn.Integer, primary_key=True)
    login1 = conn.Column(conn.String(300))
    password1 = conn.Column(conn.Integer())

    def save(self):
        conn.session.add(self)
        conn.session.commit()

    def __repr__(self):
        return f"<users {self.id}"


with app.app_context():
    conn.drop_all()
    conn.create_all()
    conn.session.commit()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/ok')
def ok():
    user = User.query.all()
    name = user[current_users].login1
    ids = user[current_users].id
    return render_template('account.html', name=name, ids=ids)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        login = request.form['login']
        password = request.form['password']

        try:
            password = int(password)
        except ValueError:
            return redirect('/nsuccessful')

        if login != '' and password != '':
            user = User.query.all()
            current_user = -1
            for i in range(0, len(user)):
                if (user[i].login1 == login) and (user[i].password1 == password):
                    current_user = i
                    break
                else:
                    current_user = -1

            if current_user != -1:
                global current_users
                current_users = current_user
                return redirect('/ok')
            else:
                return redirect('/nsuccessful')
        else:
            return redirect('/nsuccessful')
    else:
        return render_template('login.html')


@app.route('/successful')
def successful():
    return render_template('/successful.html')


@app.route('/nsuccessful')
def nsuccessful():
    return render_template('nsuccessful.html')


@app.route('/signin', methods=['POST', 'GET'])
def signin():
    if request.method == "POST":
        login = request.form['login']
        password = request.form['password']

        try:
            password = int(password)
        except ValueError:
            return redirect('/nsuccessful')

        if login != '' and password != '':
            user = User(login1=login, password1=password)
            user.save()
            return redirect('/successful')
        else:
            return redirect('/nsuccessful')
    else:
        return render_template('signin.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


if __name__ == '__main__':
    app.run('0.0.0.0')
