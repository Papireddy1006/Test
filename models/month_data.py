from db import db
from models.project_data import ProjectModel

class MonthModel(db.Model):
    __tablename__ = 'month_vice_data'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer,db.ForeignKey('projects.id'))
    project = db.relationship('ProjectModel')
    Jan_2022 = db.Column(db.Float(precision=4))
    Feb_2022 = db.Column(db.Float(precision=4))
    Mar_2022 = db.Column(db.Float(precision=4))
    Apr_2022 = db.Column(db.Float(precision=4))
    May_2022 = db.Column(db.Float(precision=4))
    Jun_2022 = db.Column(db.Float(precision=4))
    Jul_2022 = db.Column(db.Float(precision=4))
    Aug_2022 = db.Column(db.Float(precision=4))
    Sep_2022 = db.Column(db.Float(precision=4))
    Oct_2022 = db.Column(db.Float(precision=4))
    Nov_2022 = db.Column(db.Float(precision=4))
    Dec_2022 = db.Column(db.Float(precision=4))

    def __init__(self,project_id,Jan_2022,Feb_2022,Mar_2022,Apr_2022,May_2022,Jun_2022,Jul_2022,Aug_2022,Sep_2022,
                  Oct_2022,Nov_2022,Dec_2022):
        self.project_id = project_id
        self.Jan_2022 = Jan_2022
        self.Feb_2022 = Feb_2022
        self.Mar_2022 = Mar_2022
        self.Apr_2022 = Apr_2022
        self.May_2022 = May_2022
        self.Jun_2022 = Jun_2022
        self.Jul_2022 = Jul_2022
        self.Aug_2022 = Aug_2022
        self.Sep_2022 = Sep_2022
        self.Oct_2022 = Oct_2022
        self.Nov_2022 = Nov_2022
        self.Dec_2022 = Dec_2022

    def json(self):

        return {'project_id':self.project_id,
                "Jan_2022" : self.Jan_2022,
                "Feb_2022" : self.Feb_2022,
                "Mar_2022" : self.Mar_2022,
                "Apr_2022" : self.Apr_2022,
                "May_2022" : self.May_2022,
                "Jun_2022" : self.Jun_2022,
                "Jul_2022" : self.Jul_2022,
                "Aug_2022" : self.Aug_2022,
                "Sep_2022" : self.Sep_2022,
                "Oct_2022" : self.Oct_2022,
                "Nov_2022" : self.Nov_2022,
                "Dec_2022" : self.Dec_2022
                }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_project_id(cls, project_id):
        return ProjectModel.query.filter_by(id=project_id) .first() # SELECT * FROM items WHERE name=name LIMIT 1

    @classmethod
    def find_by_monthly_id(cls, project_id):
        return cls.query.filter_by(project_id=project_id) .first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()