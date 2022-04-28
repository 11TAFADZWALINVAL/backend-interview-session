# connecting to the database backendSql
from flask_sqlalchemy import SQLAlchemy
conn = SQLAlchemy.connect('Driver={SQL Server};'
                      'Server=LAPTOP-8G9HD4VB\SQLEXPRESS;'
                      'Database=backendSql;'
                      'Trusted_Connection=yes;')
 
cursor = conn.cursor()
#testing initial connection to the database
cursor.execute('SELECT * FROM Area')
 
for i in cursor:
    print(i)


# Data to initialize database with
Area = [
    {'Name': 'HarareCbd', 'City': 'Harare','District':'HARARE' 'SHOPID':'ECONET FRIST STREET'},
]
# Iterate over the Area database structure and populate the tables
for area in Area:
    p = area(Name = area['HarareCBD'],City=area['Harare'], Province=area['HARARE'],SHOPID = area['Econet first street'])
    db.session.add(p)
#save all entries created inthe database
db.session.commit()

#expossing the api as a restEndpoint
###This api is a framework based the python flask.sqlalchemy libraries
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))
# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)
# Get the underlying Flask app instance
app = connex_app.app
# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'backendSql.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # this is an event driven instance of the program so this feature is on otherwise would turn it off in non-event driven instances of apis
# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)

from flask import (
    make_response,
    abort,
)
from config import db
def read_all():
    """
    This function responds to a request for /api/backendSql
    with the complete lists of areas

    :return:        json string of list of areas
    """
    # Create the list of areas from our database
    Area = backendSQL.query \
        .order_by(Area.SHOPID) \
        .all()

    
