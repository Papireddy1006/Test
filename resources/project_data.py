from flask_restful import Resource, reqparse
from models.project_data import ProjectModel
from models.month_data import MonthModel

class Project(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('ETT_Org', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('Manager', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('US_Focal', type=str, required=True, help='This field cannot be left blank')
    # parser.add_argument('Project_Name', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('Skill_Group', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('Buissness_Unit', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('Capability', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('Forecast_Confidence', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('Comments', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('Chargeline', type=str, required=True, help='This field cannot be left blank')

    def get(self, Project_Name):
        project = ProjectModel.find_by_project(Project_Name)
        if project:
            return project.json()
        return {'message':'Project not found'}, 404

    def post(self, Project_Name):
        if ProjectModel.find_by_project(Project_Name):
            return {'message': 'A Project with name {} already existed'.format(Project_Name)}, 400
        data = Project.parser.parse_args()
        project=ProjectModel(Project_Name,**data)
        try:
            project.save_to_db()
        except:
            return {'message': 'An error occurred while creating the Project'}, 500
        return project.json(), 201


    def delete(self, Project_Name):
        project = ProjectModel.find_by_project(Project_Name)
        month = MonthModel.find_by_monthly_id(project.id)
        if project:
            project.delete_from_db()
            month.delete_from_db()
            return {'message':'Project and related data deleted'}
        return {'message':'Project not found'}, 404

    def put(self, Project_Name):
        data = Project.parser.parse_args()
        project = ProjectModel.find_by_project(Project_Name)
        if project is None:
            project = ProjectModel(Project_Name, **data)

        else:
            project.ETT_Org = data["ETT_Org"]
            project.Manager = data["Manager"]
            project.US_Focal = data["US_Focal"]
            project.Skill_Group = data["Skill_Group"]
            project.Buissness_Unit = data["Buissness_Unit"]
            project.Capability = data["Capability"]
            project.Forecast_Confidence = data["Forecast_Confidence"]
            project.Comments = data["Comments"]
            project.Chargeline = data["Chargeline"]

        project.save_to_db()

        return project.json(), 201


class ProjectList(Resource):
    def get(self):
        return {'projects': [project.json() for project in ProjectModel.find_all()]}