from fastapi import Depends, HTTPException, status, UploadFile, Form, File
from typing import Optional
from schemas import UserCreate, Post
from models import  UserModel
from models import PostModel 
from sqlalchemy.orm import Session
from database import get_db
import schemas
from uuid import UUID





class CrudService:

    @staticmethod
    def create_user(user_data: UserCreate, db: Session):
        existing_email = db.query(UserModel).filter(UserModel.email == user_data.email).first()

        if existing_email:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, details="Email already exist")
        
        user = UserModel(
            username = user_data.username,
            email =user_data.email
        )

        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    @staticmethod
    def create_post(username, title, content, image_filename, likes, db: Session):
        user = db.query(UserModel).filter(UserModel.username == username).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")       
        
        post = PostModel(
            user_id=user.id,          
            username=user.username,   
            title=title,
            content=content,
            image_filename=image_filename,
            likes=likes,
            )
        db.add(post)
        db.commit()
        db.refresh(post)
        return post
        
    
    @staticmethod
    def get_posts_by_user(username: str, db: Session):
        return db.query(PostModel).filter(PostModel.username == username).all()
    
    @staticmethod
    def get_all_posts(db: Session):
        return db.query(PostModel).all()
        
        

    @staticmethod
    def like_posts(post_id: UUID,  db: Session):
        post = db.query(PostModel).filter(PostModel.id == post_id).first()
        if post:
            post.likes +=1
            db.commit()
            db.refresh(post)
        return post 
       
    

crud_service = CrudService()


