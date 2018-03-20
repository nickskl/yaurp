from services.user import app
from flask_restful import Api


app.config['SECRET_KEY'] = 'user-service-secret'
api = Api(app)
service_namespace = "/users"


if __name__ == '__main__':
    # app.run(debug=True, ssl_context=context)
    app.run(debug=True)