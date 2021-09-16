from db import db
import pandas as pd
from flask_restful import reqparse

class ProjectModel(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    ETT_Org = db.Column(db.String(60))
    Manager = db.Column(db.String(60))
    US_Focal = db.Column(db.String(60))
    Project_Name = db.Column(db.String(60))
    Skill_Group = db.Column(db.String(60))
    Buissness_Unit = db.Column(db.String(10))
    Capability = db.Column(db.String(60))
    Forecast_Confidence = db.Column(db.String(60))
    Comments = db.Column(db.String(60))
    Chargeline = db.Column(db.String(60))


    months = db.relationship('MonthModel', lazy='dynamic')

    def __init__(self,Project_Name,ETT_Org,Manager,US_Focal,Skill_Group,Buissness_Unit,
                 Capability,Forecast_Confidence,Comments,Chargeline):
        self.Project_Name = Project_Name
        self.ETT_Org = ETT_Org
        self.Manager = Manager
        self.US_Focal = US_Focal
        self.Skill_Group = Skill_Group
        self.Buissness_Unit = Buissness_Unit
        self.Capability = Capability
        self.Forecast_Confidence = Forecast_Confidence
        self.Comments = Comments
        self.Chargeline = Chargeline

    def json(self):
        return {'id':self.id,
                "ETT_Org" : self.ETT_Org,
                "Manager" : self.Manager,
                "US_Focal" : self.US_Focal,
                "Project_Name" : self.Project_Name,
                "Skill_Group" : self.Skill_Group,
                "Buissness_Unit" : self.Buissness_Unit,
                "Capability" : self.Capability,
                "Forecast_Confidence" : self.Forecast_Confidence,
                "Comments" : self.Comments,
                "Chargeline" : self.Chargeline,
                'monthly_data': [month.json() for month in self.months.all()]}

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_project(cls, Project_Name ):
        return cls.query.filter_by(Project_Name=Project_Name).first() # SELECT * FROM items WHERE name=name LIMIT 1

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
