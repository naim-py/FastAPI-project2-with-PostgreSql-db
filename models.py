from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

# Questions Table
class Questions(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, index=True)
    
    # ✅ Define relationship (one question has many choices)
    choices = relationship("Choice", back_populates="question", cascade="all, delete")

# Choices Table
class Choice(Base):
    __tablename__ = 'choices'

    id = Column(Integer, primary_key=True, index=True)
    choice_text = Column(String, index=True)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey("questions.id"))  # ✅ Corrected column name
