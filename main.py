#import solvers.test as test
import solvers.ct as ct
import solvers.cr as cr
import solvers.S as S
import solvers.AR as AR
import solvers.TR as TR
import solvers.Afin as Afin
import solvers.Cna as Cna
import solvers.AoA as AoA
import solvers.Cn as Cn
import solvers.Ct_ as Ct
import solvers.Cl as Cl
import solvers.Cd as Cd
import solvers.Fl as Fl
import solvers.Fd as Fd
import solvers.m as m
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

api.add_resource(AR.AR_1, '/AR/1')
api.add_resource(AR.AR_2, '/AR/2')

api.add_resource(TR.TR_1, '/TR/1')
api.add_resource(TR.TR_2, '/TR/2')

api.add_resource(Afin.Afin_1, '/Afin/1')
api.add_resource(Afin.Afin_2, '/Afin/2')
api.add_resource(Afin.Afin_3, '/Afin/3')

api.add_resource(Cna.Cna_1, '/Cna/1')
api.add_resource(Cna.Cna_2, '/Cna/2')

api.add_resource(AoA.AoA_1, '/AoA/1')

api.add_resource(Cn.Cn_1, '/Cn/1')

api.add_resource(Ct.Ct_1, '/Ct/1')

api.add_resource(Cl.Cl_1, '/Cl/1')

api.add_resource(Cd.Cd_1, '/Cd/1')

api.add_resource(Fl.Fl_1, '/Fl/1')

api.add_resource(Fd.Fd_1, '/Fd/1')

api.add_resource(m.m_1, '/m/1')
api.add_resource(m.m_2, '/m/2')

if __name__ == '__main__':
    app.run(debug=False)
