from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:123@172.18.0.2/requests_from_user'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Requests(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    firma = db.Column(db.String(100), nullable=False)
    e_mail = db.Column(db.String(100), nullable=False)
    telefon	 = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    priority = db.Column(db.String(20), index=True)
    date = db.Column(db.DateTime(), index=True)
    comment = db.Column(db.Text(), index=True)
    rating = db.Column(db.Integer(), index=True)

db.create_all()


@app.route('/')
def index():
    requests = Requests.query
    return render_template('basic_table.html', title='Basic Table',
                           users=requests)


if __name__ == '__main__':
    app.run()
