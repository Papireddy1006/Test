from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.month_data import MonthModel
class Month(Resource):
    parser = reqparse.RequestParser()
    # parser.add_argument('project_id', type=int, required=True, help='Every item need a project_id')
    parser.add_argument('Jan_2022', type=float, required=True, help='This field cannot be left blank')
    parser.add_argument('Feb_2022', type=float, required=True, help='This field cannot be left blank')
    parser.add_argument('Mar_2022', type=float, required=True, help='This field cannot be left blank')
    parser.add_argument('Apr_2022', type=float, required=True, help='This field cannot be left blank')
    parser.add_argument('May_2022', type=float, required=True, help='This field cannot be left blank')
    parser.add_argument('Jun_2022', type=float, required=True, help='This field cannot be left blank')
    parser.add_argument('Jul_2022', type=float, required=True, help='This field cannot be left blank')
    parser.add_argument('Aug_2022', type=float, required=True, help='This field cannot be left blank')
    parser.add_argument('Sep_2022', type=float, required=True, help='This field cannot be left blank')
    parser.add_argument('Oct_2022', type=float, required=True, help='This field cannot be left blank')
    parser.add_argument('Nov_2022', type=float, required=True, help='This field cannot be left blank')
    parser.add_argument('Dec_2022', type=float, required=True, help='This field cannot be left blank')


    # @jwt_required()
    def get(self, project_id):
        data = MonthModel.find_by_project_id(project_id)
        if data:
            return data.json()
        return {'message':'Item not found'},404

    # @jwt_required(fresh=True)
    def post(self, project_id):
        if MonthModel.find_by_project_id(project_id):
            data = Month.parser.parse_args()
            month = MonthModel(project_id, **data)
            data_query = MonthModel.query.filter_by(project_id=project_id) .first()
            if data_query is None:
                try:
                    month.save_to_db()
                except:
                    return {'message': 'An error occurred inserting the data'}, 500  # internal server error

                return month.json(), 201
            return{'message': "data with this project exists, Use PUT option"}, 400

        return {'message': "data with this project having ID {} not exists, first create project".format(project_id)}, 400


    def delete(self,project_id):
        month = MonthModel.find_by_monthly_id(project_id)
        if month:
            month.delete_from_db()
            return {'message':'Data deleted'}
        return {'message':'Data with that ID not exist in database'},404

    def put(self,project_id):
        data = Month.parser.parse_args()
        month = MonthModel.find_by_monthly_id(project_id)

        if month is None:
            if MonthModel.find_by_project_id(project_id):
                month = MonthModel(project_id,**data)
            else:
                return {'message': "data with this project having ID {} not exists, first create project".format(project_id)}, 400
        else:
            month.project_id = project_id
            month.Jan_2022 = data['Jan_2022']
            month.Feb_2022 = data['Feb_2022']
            month.Mar_2022 = data['Mar_2022']
            month.Apr_2022 = data['Apr_2022']
            month.May_2022 = data['May_2022']
            month.Jun_2022 = data['Jun_2022']
            month.Jul_2022 = data['Jul_2022']
            month.Aug_2022 = data['Aug_2022']
            month.Sep_2022 = data['Sep_2022']
            month.Oct_2022 = data['Oct_2022']
            month.Nov_2022 = data['Nov_2022']
            month.Dec_2022 = data['Dec_2022']

        month.save_to_db()

        return month.json()


class MonthList(Resource):

    def get(self):

        months = [month.json() for month in MonthModel.find_all()]

        return months,200