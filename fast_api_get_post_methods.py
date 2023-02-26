from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
class Course(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    author: Optional[str] = None
app = FastAPI()
# course_items = [{"course_name": "Python"}, {"course_name1": "sqlalchemy"}, {"course_name2": "Nodejs"}]
course_items = [{"course_name": "Python"}, {"course_name1": "sqlalchemy"}, {"course_name2": "Nodejs"},{"course_name3":"Javs"}]
@app.post("/courses")
def create_course(course: Course):
    return course
@app.get("/courses/{course_name}")
def read_course(course_name):
    return{"course_name": course_items}
# def read_course(start:int,end:int):
#     return course_items[start:start + end]
if __name__ == "__main__":
 uvicorn.run(app=app, host="127.0.0.1", port=7000)