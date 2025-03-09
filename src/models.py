
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, String, ForeignKey
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    password:Mapped[str]=mapped_column(nullable=False)

    favorites = relationship("Favoritos", back_populates="user")



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

class Episode(db.Model):
    __tablename__ = "episode"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    air_date: Mapped[str] = mapped_column(String, nullable=False)
    episode: Mapped[str] = mapped_column(String, nullable=False)
    url: Mapped[str] = mapped_column(String, nullable=False)
    created: Mapped[str] = mapped_column(String, nullable=False)

    


class Location(db.Model):
    __tablename__ ="location"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)
    dimension: Mapped[str] = mapped_column(String, nullable=False)
    url: Mapped[str] = mapped_column(String, nullable=False)
    created: Mapped[str] = mapped_column(String, nullable=False)


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


