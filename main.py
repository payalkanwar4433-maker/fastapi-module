from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    email: str

@app.post("/users")
def create_user(user: User):
    return user
from fastapi import FastAPI
app=FastAPI()
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    Name: str
    age: int

@app.get("/")
def home():
    return{"message":"Hello fastapi"}

@app.get("/about")
def about():
    return{"message":"Hello from about page"}
#Optional parameter
@app.get("/user/{user_id}")
def about(user_id:int):
    return{"user_id":user_id}


@app.get("/users")

def users(name:str=None):
    return{
        "Name":name
    }

#dafault values
@app.get("/products")
def products(limit:int=10):
    return{"Limit":limit}

@app.get("/items")
def products(name:str=None,price:int=10):
    return{
        "Name":name,
        "Price":price}

@app.post("/created-user")
def create_user(user:User):
    return{
        "message":"User Created",
        "data":user
        }
        
class User(BaseModel):
    name:str
    age:int
    email:str
@app.post("/create_user")    
def create_user(user:User):
    return{
        "message":"User Created",
        "data":user
    }    
class Address(BaseModel):
    city:str
    pincode:int

class User(BaseModel):
    name:str
    age:int
    address:Address

@app.post("/create_user")  
def create_user(user:User):
    return user
todos=[]
class Todo(BaseModel):
    id:int
    title:str
    completed:bool
@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return {"message":"TODO ADDED","data":todo}

@app.get("/todos")
def get_todos():
    return todos

@app.get("/todos/{todos_id}")
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id==todo_id:
            return todo
    return {"message":"Todo not found"}    

@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,updated_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id==todo_id:
            todos[index]=updated_todo
            return{
                "message":"Data Updated",
                "data":updated_todo
            }
    return {"error":"Todo not found"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for index,todo in enumerate(todos):
        if todo.id==todo_id:
            todos.pop(index)
            return{
                "message":"Data Deleted",
            }
    return {"error":"Todo not found"}

# PATH + QUERY + BODY COMBO
users=[]

class User(BaseModel):
    name:str
    age:int
@app.post("/users")
def create_user(user:User):
    users.append(user)
    return{
        "message":"User Created",
        "data":user
    }

@app.put("/users/{user_id}")
def updated_user(user_id:int,user:User,notify:bool=False):
    if user_id<len(users):
        users[user_id]=user

        return{
            "message":"User Updated",
            "notify":notify,
            "data":user
        }
    return{
        "error":"User not Found"
    }

# RESPONSE MODELS CONCEPTS

class User(BaseModel):
    name:str
    age:int
    password:str

class UserResponse(BaseModel):
    name:str
    age:int

@app.get("/user",response_model=UserResponse)
def get_user():
    return{
        "name":["payal","anjali"],
        "name":"Mohit",
        "age":24,
        "password":"123456"
    }