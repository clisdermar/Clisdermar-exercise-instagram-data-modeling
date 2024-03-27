import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy import Enum

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname =  Column(String(250), nullable=False)
    last_name=Column(String(80),nullable=False)
    email=Column(String(80),nullable=False)
     

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id= Column(Integer)

    user_id = Column(Integer , ForeignKey('user.id'))
    User = relationship(User)

class Follower(Base):
    __tablename__ = 'follower'
    
   
    user_from_id = Column(Integer, primary_key= True )
   

    user_to_id= Column(Integer , ForeignKey('user.id'))
    User = relationship("User")

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key = True)
    comment_text = Column(String(250),nullable = False)
   
    author_id = Column(Integer , ForeignKey('user.id'))
    User = relationship(User)
    
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

    def to_dict(self):
        return {}

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key= True)
    type = Column(Enum('video','video'))
    url = Column(String(250),nullable = False)

    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship (Post)



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
