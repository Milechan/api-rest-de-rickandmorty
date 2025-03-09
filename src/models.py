
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, String, ForeignKey
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False,unique=True)
    password:Mapped[str]=mapped_column(nullable=False)

    favorites = relationship("Favoritos", back_populates="user")
    
    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "email":self.email,
            "password":self.password
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Character(db.Model):
    __tablename__ = 'character'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)
    species: Mapped[str] = mapped_column(String, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=True)
    gender: Mapped[str] = mapped_column(String, nullable=False)
    origin: Mapped[str] = mapped_column(String, nullable=True)
    location: Mapped[str] = mapped_column(String, nullable=True)
    image: Mapped[str] = mapped_column(String, nullable=False)
    url: Mapped[str] = mapped_column(String, nullable=False)
    created: Mapped[str] = mapped_column(String, nullable=False)

    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "status":self.status,
            "gender":self.gender,
            "origin":self.origin,
            "location":self.location,
            "image":self.image,
            "url":self.url,
            "created":self.created
        }
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Episode(db.Model):
    __tablename__ = "episode"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    air_date: Mapped[str] = mapped_column(String, nullable=False)
    episode: Mapped[str] = mapped_column(String, nullable=False)
    url: Mapped[str] = mapped_column(String, nullable=False)
    created: Mapped[str] = mapped_column(String, nullable=False)

    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "air_date":self.air_date,
            "episode":self.episode,
            "url":self.url,
            "created":self.created
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()



class Location(db.Model):
    __tablename__ ="location"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)
    dimension: Mapped[str] = mapped_column(String, nullable=False)
    url: Mapped[str] = mapped_column(String, nullable=False)
    created: Mapped[str] = mapped_column(String, nullable=False)

    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "type":self.type,
            "dimension":self.dimension,
            "url":self.url,
            "created":self.created
        }
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Favoritos(db.Model):
    __tablename__ ="favoritos"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"), nullable=True)
    location_id: Mapped[int] = mapped_column(ForeignKey("location.id"), nullable=True)
    episode_id: Mapped[int] = mapped_column(ForeignKey("episode.id"), nullable=True)

    user = relationship("User",back_populates="favorites")
    character = relationship("Character")
    location = relationship("Location")
    episode = relationship("Episode")

    def serialize(self):
        return {
            "id":self.id,
            "user_id":self.user_id,
            "character_id":self.character_id,
            "location_id":self.location_id,
            "episode_id":self.episode_id
            
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
