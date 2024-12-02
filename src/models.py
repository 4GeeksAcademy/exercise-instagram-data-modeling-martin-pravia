import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(120), nullable=False)
    firstname = Column(String(120), nullable=False)
    lastname = Column(String(120), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    
class Comment(Base):
    __tablename__ = "Comment"
    id = Column(Integer, primary_key=True, nullable=False)
    comment_text = Column(String)
    author_id = Column(Integer, ForeignKey("User.id"))
    post_id = Column(Integer, ForeignKey("Post.id"))
    user = relationship("User", backref="comment")
    post = relationship("Post", backref = "comment")

class Post(Base):
    __tablename__ = "Post"
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)
    user = relationship("User", backref="post")

class Media(Base):
    __tablename__ = "Media"
    id = Column(Integer, primary_key=True, nullable=False)
    type = Column(Enum)
    url = Column(String(150))
    post_id = Column(Integer, ForeignKey("Post.id"), nullable=False)
    post = relationship("Post", backref="media")

class Follower(Base):
    __tablename__ = "Follower"
    user_form_id = Column(Integer, ForeignKey("User.id"), primary_key=True, nullable=False)
    user_to_id = Column(Integer,ForeignKey("User.id"), primary_key= True, nullable=False)
    user_form = relationship("User", backref="follower")
    user_to = relationship("User", backref="follower")
    
        

    
    
    








## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
