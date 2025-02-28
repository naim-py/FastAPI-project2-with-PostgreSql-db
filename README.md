# FastAPI-project2-with-PostgreSql-db
# FastAPI with PostgreSQL - Quiz Application

This is a simple FastAPI project with PostgreSQL integration for managing quiz questions and choices.

## Features
- Create questions with multiple choices
- Retrieve questions and their choices
- Uses SQLAlchemy for database interactions

## Prerequisites
Before running the application, ensure you have the following installed:
- Python 3.8+
- PostgreSQL
- `pip` (Python package manager)

## Installation

### 1. Clone the Repository
```sh
git clone https://github.com/your-repo/fastapi-quiz-app.git
cd fastapi-quiz-app

# 2. Set Up Virtual Environment
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Configure PostgreSQL Database
URL_DATABASE= 'postgresql://<username>:<password>@localhost:<port>/<database_name>'

# 5. Run the Application
uvicorn main:app --reload
