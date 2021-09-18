
from flask import Flask
from flask_restful import Api

from resources.month_data import Month, MonthList
from resources.project_data import Project, ProjectList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:papiai20@localhost/innersource1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

app.config['SECRET_KEY'] = 'jose'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Project, '/project/<string:Project_Name>')
api.add_resource(Month, '/month/<string:Project_Name>')
api.add_resource(MonthList, '/months')
api.add_resource(ProjectList, '/projects')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
