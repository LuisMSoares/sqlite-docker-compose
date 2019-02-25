from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def data(self):
        return "Nome: {} <br>".format(self.name)

@app.route('/add')
def Insert():
    u1 = User(name='João')
    u2 = User(name='Maria')
    u3 = User(name='Jose')

    add(u1)
    add(u2)
    add(u3)

    return 'Dados adicionados'

@app.route('/view')
def Select():
    result = User.query.all()
    html = ''

    for r in result:
        html += r.data()

    return html



def add(obj):
    db.session.add(obj)
    db.session.commit()


if __name__ == '__main__':
    try:
        db.create_all()
    except:
        ...
    app.run(host='0.0.0.0', port=5000, debug=True)