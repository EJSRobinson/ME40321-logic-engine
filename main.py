import solvers.test as test
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class core(Resource):
    def get(self):
        return test.myTestFunction()


api.add_resource(core, '/test')

if __name__ == '__main__':
    app.run(debug=True)
