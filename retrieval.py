#service for retrieving all shops created under a specific area and expose the service through a rest endpoint

#response server
from flask import (
    Flask,
    render_template
)
# response application instance
app = Flask(__name__, template_folder="templates")

#using the connexion library to create the rest endpoint
#$ pip3 install connexion[swagger-ui]-- to istall the library
from flask import render_template
import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# Create a URL route in our application for "/"
# run the appliation service in standalone mode.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

#api handlers
from datetime import datetime
def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
AREAS = {
    "HARARE CBD": {
        "Name": "CBD",
        "SHOPID": "CBD",
        "timestamp": get_timestamp()
    },
    
}

# Create a handler for our read (GET) AREAS
def read():
    # Create the list of AREAS from our data
    return [AREAS[key] for key in sorted(AREAS.keys())]