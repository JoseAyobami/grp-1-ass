from fastapi import FastAPI, Depends, HTTPException, status, UploadFile, Form, File
from schemas import UserCreate, Post
from database import get_db, engine
from sqlalchemy.orm import Session
from crud import crud_service
from pydantic import Field
from typing import Optional, List
import models
from uuid import UUID

import os
import shutil
import uuid

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)



models.Base.metadata.create_all(engine)

app = FastAPI(title="Social Media API")

@app.post("/user", status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return crud_service.create_user(user_data, db)



@app.post("/post", response_model=Post)
def create_post(
    username: str = Form(...),
    title: str = Form(...),
    content: str = Form(...),
    image: UploadFile = File(None),
    db: Session = Depends(get_db)
    ):
    image_path = None
    if image:
        image_path = os.path.join(UPLOAD_DIR, image.filename)
        with open(image_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
    post = crud_service.create_post(username, title, content, image, image_path, db)

    if not post:
        raise HTTPException(status_code=404, detail="User not found")

    return post

@app.get("/posts/",  response_model=List[Post])
def get_all_posts(db: Session = Depends(get_db)):
    return crud_service.get_all_posts(db)
    

@app.get("/user/{username}posts", response_model=List[Post])
def get_users_post(username: str, db: Session = Depends(get_db)):
    return crud_service.get_posts_by_user(username, db) 


@app.get("/posts/{post_id}like")
def create_post_like(post_id: UUID,  db: Session = Depends(get_db)):
    return crud_service.like_posts(post_id, db)