from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, and_, or_, not_
from sqlalchemy import MetaData, Table, select, text

db = SQLAlchemy()

class DB_Data():
    engine = create_engine('mysql+pymysql://root:papiai20@localhost/innersource1')
    conn = engine.connect()
    metadata = MetaData()

    projects = Table("projects", metadata, autoload=True, autoload_with=engine)
    data_2022 = Table("data_2022", metadata, autoload=True, autoload_with=engine)

    query_string = text("""SELECT p.id, p.ETT_Org, p.Manager, p.US_Focal, p.Project_Name, p.Skill_Group, p.Buissness_Unit, p.Capability,
    p.Forecast_Confidence, p.Comments, p.Chargeline,d.Jan_2022, d.Feb_2022, d.Mar_2022, d.Apr_2022, d.May_2022,
    d.Jun_2022, d.Jul_2022, d.Aug_2022, d.Sep_2022, d.Oct_2022, d.Nov_2022, d.Dec_2022 
    FROM projects p left join data_2022 d
    on p.Project_Name=d.Project_Name""")

    total_db_data = conn.execute(query_string).fetchall()
    total_db_headings=("id", "ETT_Org", "Manager", "US_Focal", "Project_Name", "Skill_Group", "Buissness_Unit", "Capability",
                       "Forecast_Confidence", "Comments", "Chargeline","Jan_2022", "Feb_2022", "Mar_2022", "Apr_2022",
                       "May_2022", "Jun_2022", "Jul_2022", "Aug_2022", "Sep_2022", "Oct_2022", "Nov_2022", "Dec_2022")
# for row in total_db_data:
#     print(row)

