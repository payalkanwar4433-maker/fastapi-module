from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def home():
    return{"message":"Hello fastapi"}

@app.get("/about")
def about():
    return{"message":"Hello from about page"}

@app.get("/users")
def users():
    return{
        "name":["payal","anjali"]
    }
