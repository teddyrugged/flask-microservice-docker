from flask import Flask
from src.database.db import initialize_db
from src.urls.routes import initialize_routes
from flask_restful import Api
from flask_pymongo import PyMongo
# config = configparser.ConfigParser()
# config.read(os.path.abspath(os.path.join(".env")))


app = Flask(__name__)

# database configuration
app.config["MONGODB_SETTINGS"] = MONGO_URI ={
    "db": "Order-Product-db",
    "host": "localhost",
    "port": 27017
}
# app.config["MONGODB_SETTINGS"] = MONGO_URI ={
#     "mongodb+srv://Josiah:<Holycraft@30>@cluster0.domeb8u.mongodb.net/?retryWrites=true&w=majority"
# }

api = Api(app,)

initialize_db(app)
initialize_routes(api)


app.run(host="127.0.0.1", port=5000, debug=True)
