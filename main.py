from flask import Flask, url_for, request, render_template, json
from flask import redirect
from data import db_session

from data.users import User
from data.news import News

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
@app.route('/index')
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private != True)
    return render_template("index.html", news=news)



def main():
    db_session.global_init("db/blogs.db")
    app.run(port=8000, host='127.0.0.1')


if __name__ == '__main__':
    main()