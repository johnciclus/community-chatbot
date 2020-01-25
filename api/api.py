from flask import Flask
from flask_restful import Api
from resources import Message, Messages

app = Flask(__name__)
api = Api(app)
api.add_resource(Messages, '/api/messages/')
api.add_resource(Message, '/api/messages/<int:id>', endpoint='message_endpoint')

if __name__ == '__main__':
    app.run(debug=True)