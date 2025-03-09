from flask import Flask
from flask_migrate import Migrate
from models import db


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///database.db"

db.init_app(app)
Migrate(app,db)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"






if __name__ =="__main__":
    app.run(host="127.0.0.1")