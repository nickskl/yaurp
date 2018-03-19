import flask


app = flask.Flask(__name__)
service_namespace = "/posts"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/posts_db'


if __name__ == '__main__':
    app.run(debug=True)