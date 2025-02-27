from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Emotions(BaseModel):
    Happiness: float = Field(default=0.0)
    Sadness: float = Field(default=0.0)
    Fear: float = Field(default=0.0)
    Anger: float = Field(default=0.0)
    Surprise: float = Field(default=0.0)
    Disgust: float = Field(default=0.0)
    Contempt: float = Field(default=0.0)
    Anticipation: float = Field(default=0.0)
    Suicidality: float = Field(default=0.0)

class UserContext(BaseModel):
    name: str = Field(default="")
    age: str = Field(default="")

class CalendarInput(BaseModel):
    start_datetime : datetime = Field(default=None)
    end_datetime : datetime = Field(default=None)
    title : str = Field(default=None)
    description : str = Field(default=None)

class ChatResponse(BaseModel):
    user: UserContext = Field(default=UserContext())
    response: str = Field(default=None)
    updated_context : str = Field()
    calendar_event : Optional[CalendarInput] = Field(default={})

class ChatResponseStr(BaseModel):
    response : str = Field(default="I'm having some trouble atm, Please try later")