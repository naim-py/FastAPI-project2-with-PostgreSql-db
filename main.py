from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session  

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# ✅ Request Models
class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool

class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]

# ✅ Dependency for Database Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/questions/{question_id}")
async def read_question(question_id: int, db: Session = Depends(get_db)):
    result = db.query(models.Questions).filter(models.Questions.id == question_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Question not found")
    return result

@app.get("/choices/{question_id}")
async def read_choices(question_id: int, db: Session = Depends(get_db)):
    result = db.query(models.Choice).filter(models.Choice.question_id == question_id).all()
    if not result:
        raise HTTPException(status_code=404, detail="Choices not found")
    return result

#first
@app.post("/questions/")
async def create_questions(question: QuestionBase, db: Session = Depends(get_db)):
    try:
        db_question = models.Questions(question_text=question.question_text)
        db.add(db_question)
        db.commit()
        db.refresh(db_question)

        for choice in question.choices:
            db_choice = models.Choice(
                choice_text=choice.choice_text,
                is_correct=choice.is_correct,
                question_id=db_question.id
            )
            db.add(db_choice)

        db.commit()
        return {"message": "Question and choices created successfully", "question_id": db_question.id}

    except Exception as e:
        db.rollback()  # Rollback changes if an error occurs
        import traceback
        print("Error inserting data:", str(e))  # Print the error
        traceback.print_exc()  # Show full traceback
        raise HTTPException(status_code=500, detail=f"Database insertion failed: {str(e)}")
