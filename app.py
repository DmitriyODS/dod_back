from typing import List, Any, Tuple

from flask import Flask, render_template, request, redirect, url_for, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from werkzeug import Response


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:lkop123@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'iuk2.master.class@gmail.com'
app.config['MAIL_PASSWORD'] = '123'


class User(db.Model):
    __tablename__ = 'demo'
    user_id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String(255))
    email = db.Column(db.String(255))
    city = db.Column(db.String(255))
    school = db.Column(db.String(255))
    is_finished = db.Column(db.Boolean)
    type_mk = db.Column(db.Boolean)


@app.route('/admin_panel', methods=['GET', 'POST'])
def admin_panel():
    return render_template('admin.html', users_count=get_users_count(), users=get_user_list_finished())


@app.route('/finish/<int:user_id>', methods=['POST'])
def finish(user_id: int) -> Response | tuple[Response, int]:
    try:
        user = User.query.get(user_id)
        if user:
            user.is_finished = not user.is_finished
            db.session.commit()
        else:
            return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/get_user_list', methods=['GET'])
def get_user_list_finished() -> tuple[Response, int] | Any:
    try:
        users = User.query.filter_by(is_finished=False).all()
        return users
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/get_users_count', methods=['GET'])
def get_users_count():
    try:
        response = User.query.count()
        return response

    except:
        response = 'Error'
        return response


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        fio = request.form['fio']
        school = request.form['school']
        city = request.form['city']
        email = request.form['email']
        type_mk = request.form['type_mk']

        new_user = User(fio=fio,
                        email=email,
                        city=city,
                        school=school,
                        is_finished=0,
                        type_mk=bool(int(type_mk))
                        )
        db.session.add(new_user)
        db.session.commit()

        return render_template('confirmation.html',
                               fio=fio,
                               school=school,
                               city=city,
                               email=email,
                               name_type_mk=type_mk)

    return render_template('index.html', users_count=get_users_count())


if __name__ == '__main__':
    app.run(debug=True)
