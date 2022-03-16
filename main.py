#import solvers.test as test
import solvers.ct as ct
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


api.add_resource(ct.ct_1, '/ct/1')

if __name__ == '__main__':
    app.run(debug=True)
