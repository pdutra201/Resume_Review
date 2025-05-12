from routes.AI_Route import AI_Route
from config import *

api.add_resource(AI_Route, "/api/request")



if __name__ == "__main__":
    app.run(debug=True)
