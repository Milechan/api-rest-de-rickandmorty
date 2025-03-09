from flask import Flask
from flask_migrate import Migrate
from models import db,User,Location,Character,Episode,Favoritos
from flask import request,json,jsonify
import os
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///database.db"

db.init_app(app)
Migrate(app,db)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



@app.route("/characters",methods=["GET"])
def obtener_personajes_todos():
    pass

@app.route("/characters/<int:character_id>",methods=["GET"])
def obtener_personaje(character_id):
    pass


@app.route("/episodes",methods=["GET"])
def obtener_episodios_todos():
    pass

@app.route("/episodes/<int:episode_id>",methods=["GET"])
def obtener_episodio(episode_id):
    pass


@app.route("/locations",methods=["GET"])
def obtener_lugares_todos():
    pass

@app.route("/locations/<int:location_id>",methods=["GET"])
def obtener_lugar(location_id):
    pass


@app.route("/users",methods=["GET"])
def obtener_usuarios_todos():
    pass


@app.route("/users/favorites",methods=["GET"])
def obtener_favoritos_usuario():
    pass



@app.route("/favorite/character/<int:character_id>",methods=["POST"])
def agregar_personaje_favorito(character_id):
    pass

@app.route("/favorite/episode/<int:episode_id>",methods=["POST"])
def agregar_episodio_favorito(episode_id):
    pass

@app.route("/favorite/location/<int:location_id>",methods=["POST"])
def agregar_lugar_favorito(location_id):
    pass

@app.route("/favorite/character/<int:character_id>",methods=["DELETE"])
def eliminar_personaje_favorito(character_id):
    pass

@app.route("/favorite/episode/<int:episode_id>",methods=["DELETE"])
def eliminar_episodio_favorito(episode_id):
    pass

@app.route("/favorite/location/<int:location_id>",methods=["DELETE"])
def eliminar_lugar_favorito(location_id):
    pass


if __name__ =="__main__":
    app.run(host="127.0.0.1")