#import solvers.test as test
import solvers.ct as ct
import solvers.cr as cr
import solvers.S as S
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


api.add_resource(ct.ct_1, '/ct/1')
api.add_resource(ct.ct_2, '/ct/2')
api.add_resource(ct.ct_3, '/ct/3')

api.add_resource(cr.cr_1, '/cr/1')
api.add_resource(cr.cr_2, '/cr/2')
api.add_resource(cr.cr_3, '/cr/3')

api.add_resource(S.S_1, '/S/1')
api.add_resource(S.S_2, '/S/2')

if __name__ == '__main__':
    app.run(debug=False)
