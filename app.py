
from flask import Flask, render_template, request
from flask_restful import Api
import pandas as pd
import xlrd

from resources.month_data import Month, MonthList
from resources.project_data import Project, ProjectList
from models.project_data import ProjectModel
from models.month_data import MonthModel
from db_total_data import DB_Data

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


@app.route('/upload', methods = ['GET','POST'])
def index():
    return render_template("upload.html")


@app.route('/data', methods = ['GET','POST'])
def data():
    if request.method == 'POST':
        file = request.form['upload_file']
        data = pd.read_excel(file)

        for project_name in data['Project_Name']:
            data_project = ProjectModel.find_by_project(project_name)
            data_month = MonthModel.find_by_data_project_name(project_name)
            if data_month:
                data_month.delete_from_db()
            if data_project:
                data_project.delete_from_db()

        data_project_db = data[['id', "ETT_Org", "Manager", "Project_Name","US_Focal", "Skill_Group", "Buissness_Unit",
                     "Capability", "Forecast_Confidence", "Comments", "Chargeline"]]
        for x in range(len(data_project_db)):
            row_data = list(dict(data_project_db.iloc[x]).values())
            row_values = ProjectModel(row_data[3],row_data[1],row_data[2],row_data[4],row_data[5],
                                      row_data[6],row_data[7],row_data[8],row_data[9],row_data[10])
            row_values.save_to_db()

        data_month_db = data[["Project_Name","Jan_2022","Feb_2022","Mar_2022","Apr_2022","May_2022","Jun_2022","Jul_2022","Aug_2022","Sep_2022",
                             "Oct_2022","Nov_2022","Dec_2022"]]
        for x in range(len(data_month_db)):
            row_data2 = list(dict(data_month_db.iloc[x]).values())
            row_values2 = MonthModel(row_data2[0], row_data2[1], row_data2[2], row_data2[3], row_data2[4], row_data2[5], row_data2[6],
                                     row_data2[7], row_data2[8], row_data2[9], row_data2[10], row_data2[11], row_data2[12])
            row_values2.save_to_db()

        return render_template('data.html', headings=DB_Data.total_db_headings, data=DB_Data.total_db_data, refresh=False)

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
