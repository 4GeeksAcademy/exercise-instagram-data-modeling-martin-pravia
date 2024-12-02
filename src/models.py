import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column(String(120), nullable=False)
    firstname = Column(String(120), nullable=False)
    lastname = Column(String(120), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    
class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    comment_text = Column(String)
    author_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
    user = relationship("User", backref="comments")
    post = relationship("Post", backref = "comments")

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", backref="posts")

class Media(Base):
    __tablename__ = "medias"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    type = Column(Enum, nullable=False)
    url = Column(String(150), nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    post = relationship("Post", backref="medias")

class Follower(Base):
    __tablename__ = "followers"
    user_form_id = Column(Integer, ForeignKey("users.id"), primary_key=True, nullable=False)
    user_to_id = Column(Integer,ForeignKey("users.id"), primary_key= True, nullable=False)
    user_form = relationship("User", backref="following")
    user_to = relationship("User", backref="followers")
    
        

    
    
    








## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
