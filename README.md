# Social Media API

This is a simple social media API built with Python and FastAPI. It allows users to create accounts, create posts, and like posts.

## Features

*   User creation
*   Post creation (with image uploads)
*   Liking posts
*   Retrieving all posts
*   Retrieving posts by a specific user

## Project Structure

```
.
├── alembic/
├── uploads/
├── .gitignore
├── alembic.ini
├── app.py
├── crud.py
├── database.py
├── main.py
├── models.py
├── route.py
└── schemas.py
```

## Getting Started

### Prerequisites

*   Python 3.8+
*   PostgreSQL (or another SQLAlchemy-compatible database)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**

    Create a `requirements.txt` file with the following content:

    ```
    fastapi
    uvicorn
    sqlalchemy
    psycopg2-binary
    pydantic
    python-dotenv
    alembic
    python-multipart
    ```

    Then, install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up the database:**

    *   Create a `.env` file in the root directory.
    *   Add your database URL to the `.env` file:

        ```
        DATABASE_URL=postgresql://user:password@host:port/database
        ```

5.  **Run the database migrations:**

    ```bash
    alembic upgrade head
    ```

### Running the Application

To run the application, use the following command:

```bash
uvicorn route:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Users

*   `POST /user`

    Creates a new user.

    **Request Body:**

    ```json
    {
      "username": "your_username",
      "email": "your_email@example.com"
    }
    ```

### Posts

*   `POST /post`

    Creates a new post. This is a form-data request.

    **Form Data:**

    *   `username`: The username of the post creator.
    *   `title`: The title of the post.
    *   `content`: The content of the post.
    *   `image`: (Optional) An image file to upload.

*   `GET /posts/`

    Retrieves all posts.

*   `GET /user/{username}posts`

    Retrieves all posts by a specific user.

*   `GET /posts/{post_id}like`

    Likes a specific post.
