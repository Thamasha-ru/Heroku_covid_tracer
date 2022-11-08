from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

users = {
    1: {
        "name": "john",
        "age": 17,
        "class": "Year 12"
    }

}


class user(BaseModel):
    name: str
    age: int
    year: str


class Updateuser(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


@app.get("/")
def index():
    return {"name": "First Data"}


@app.get("/get-user/{user_id}")
def get_user(user_id: int = Path(None, description="The ID of the user ")):
    return users[user_id]


@app.get("/get-by-name/{user_id}")
def get_user(*, user_id: int, name: Optional[str] = "None", test: int):
    for user_id in users:
        if users[user_id]["name"] == name:
            return users[user_id]
        return {"Data": "Not found"}


@app.post("/create-user{user_id}")
def create_user(user_id: int, user: user):
    if user_id in users:
        return {"Error": "user exists"}

    users[user_id] = user
    return users[user_id]


@app.put("/update-user/{user_id")
def update_user(user_id: int, user: Updateuser):
    if user_id not in users:
        return {"Error": "user does not exist"}

    if user.name != None:
        users[user_id].name = user.name

    if user.age != None:
        users[user_id].age = user.age

    if user.year != None:
        users[user_id].year = user.year

    return users[user_id]


@app.delete("/delete-user/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        return {"Error": "user does not exist"}

    del users[user_id]
    return {"Message": "user deleted successfully"}
