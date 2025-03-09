from flask import Flask
from flask_migrate import Migrate
from models import db,User,Location,Character,Episode,Favoritos
from flask import request,json,jsonify
import os
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///database.db"

db.init_app(app)
Migrate(app,db)

with app.app_context():
    db.create_all()
print(os.path.abspath("database.db"))

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/register",methods=["POST"])
def registrar_usuario():
    # obtengo datos del body
    nombre = request.json.get("name",None)
    correo = request.json.get("email",None)
    password = request.json.get("password",None)

    # validar si existe un usuario con ese correo
    if User.query.filter_by(email=correo).one_or_none() is not None:
        return jsonify({"error": f"ya existe un usuario con el email {correo}"}),409
    # creo y guardo nuevo usuario
    nuevo_usuario = User()
    nuevo_usuario.name=nombre
    nuevo_usuario.email=correo
    nuevo_usuario.password=password
    nuevo_usuario.save()

    # respondo con el nuevo usuario guardado
    return jsonify(nuevo_usuario.serialize()),201


@app.route("/characters",methods=["GET"])
def obtener_personajes_todos():
    personajes = Character.query.all()
    lista_personajes = list(map(lambda personaje: personaje.serialize(),personajes))
    return jsonify(lista_personajes),200

@app.route("/characters/<int:character_id>",methods=["GET"])
def obtener_personaje(character_id):
    personaje = Character.query.filter_by(id=character_id).one_or_none()
    if personaje is None:
        return jsonify({"error": f"no se encontro el personaje con id {character_id}"}), 404
    return jsonify(personaje), 200


@app.route("/episodes",methods=["GET"])
def obtener_episodios_todos():
    episodio = Episode.query.all()
    lista_episodios=list(map(lambda episodio: episodio.serialize(),episodio))
    return jsonify(lista_episodios),200



@app.route("/episodes/<int:episode_id>",methods=["GET"])
def obtener_episodio(episode_id):
    episodio=Episode.query.filter_by(id=episode_id).one_or_none()
    if episodio is None:
        return jsonify({"error":f"no se encontro el episodio con id {episode_id}"}),404
    return jsonify(episodio),200

@app.route("/locations",methods=["GET"])
def obtener_lugares_todos():
    location = Location.query.all()
    lista_location=list(map(lambda location: location.serialize(),location))
    return jsonify(lista_location),200

@app.route("/locations/<int:location_id>",methods=["GET"])
def obtener_lugar(location_id):
    location=Location.query.filter_by(id=location_id).one_or_none()
    if location is None:
        return jsonify({"error":f"no se encontro el episodio con id {location_id}"}),404
    return jsonify(location),200



@app.route("/users",methods=["GET"])
def obtener_usuarios_todos():
    usuarios = User.query.all()
    lista_usuarios = list(map(lambda usuario: usuario.serialize(),usuarios))
    return jsonify(lista_usuarios),200


# @app.route("/users/favorites",methods=["GET"])
# def obtener_favoritos_usuario():
#     pass

##
## RUTAS PARA FAVORITOS
##


@app.route("/favorite/character/<int:character_id>",methods=["POST"])
def agregar_personaje_favorito(character_id):
    user_id = request.json.get("user_id",None)
    nuevo_favorito = Favoritos()
    nuevo_favorito.user_id=user_id
    nuevo_favorito.character_id=character_id
    nuevo_favorito.location_id=None
    nuevo_favorito.episode_id=None
    nuevo_favorito.save()

    return jsonify(nuevo_favorito.serialize()),201


@app.route("/favorite/episode/<int:episode_id>",methods=["POST"])
def agregar_episodio_favorito(episode_id):
    user_id = request.json.get("user_id",None)
    nuevo_favorito = Favoritos()
    nuevo_favorito.user_id=user_id
    nuevo_favorito.character_id=None
    nuevo_favorito.location_id=None
    nuevo_favorito.episode_id=episode_id
    nuevo_favorito.save()

    return jsonify(nuevo_favorito.serialize()),201

@app.route("/favorite/location/<int:location_id>",methods=["POST"])
def agregar_lugar_favorito(location_id):
    user_id = request.json.get("user_id",None)
    nuevo_favorito = Favoritos()
    nuevo_favorito.user_id=user_id
    nuevo_favorito.character_id=None
    nuevo_favorito.location_id=location_id
    nuevo_favorito.episode_id=None
    nuevo_favorito.save()

    return jsonify(nuevo_favorito.serialize()),201

@app.route("/favorite/character/<int:character_id>",methods=["DELETE"])
def eliminar_personaje_favorito(character_id):
    user_id = request.json.get("user_id",None)
    favorito=Favoritos.query.filter_by(id=character_id,user_id=user_id).one_or_none()
    if favorito is None:
        return jsonify ({"error":"no se encontro el favorito con ese id de personaje y usuario"}),404
    favorito.delete()
    return jsonify({"mensaje":"se borro exitosamente"}),200
    


@app.route("/favorite/episode/<int:episode_id>",methods=["DELETE"])
def eliminar_episodio_favorito(episode_id):
    user_id = request.json.get("user_id",None)
    favorito=Favoritos.query.filter_by(id=episode_id,user_id=user_id).one_or_none()
    if favorito is None:
        return jsonify ({"error":"no se encontro el favorito con ese id de episodio y usuario"}),404
    favorito.delete()
    return jsonify({"mensaje":"se borro exitosamente"}),200

@app.route("/favorite/location/<int:location_id>",methods=["DELETE"])
def eliminar_lugar_favorito(location_id):
    user_id = request.json.get("user_id",None)
    favorito=Favoritos.query.filter_by(id=location_id,user_id=user_id).one_or_none()
    if favorito is None:
        return jsonify ({"error":"no se encontro el favorito con ese id de location y usuario"}),404
    favorito.delete()
    return jsonify({"mensaje":"se borro exitosamente"}),200


if __name__ =="__main__":
    app.run(host="127.0.0.1")