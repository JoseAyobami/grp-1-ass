from sqlalchemy import Column, String, UUID, Integer, Text, ForeignKey
from database import Base
from sqlalchemy.orm import relationship
import uuid




class UserModel(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    

    post = relationship("PostModel", back_populates="user")





class PostModel(Base):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    username = Column(String(50), nullable=False)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)   
    image_filename = Column(String, nullable=True)
    likes = Column(Integer, nullable=False, default=0)

    user = relationship("UserModel", back_populates="post")


    


