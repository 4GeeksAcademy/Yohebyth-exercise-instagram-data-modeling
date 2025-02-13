import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__='user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32), unique=True, nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname =  Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=True) 

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    title = Column(String(250), nullable=True)
    user = relationship(User)

class Media(Base):
    __tablename__ = 'media'

    id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    url = Column(String(250), nullable=False)
    post = relationship(Post)

class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    media_id = Column(Integer, ForeignKey('media.id'))
    textcomment = Column(String(250), nullable=False)
    likes = Column(Integer, nullable=True)
    user = relationship(User)
    media = relationship(Media)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
