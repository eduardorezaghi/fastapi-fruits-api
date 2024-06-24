from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from src import database
from src import models, schemas

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to this fantastic app!"}

@app.post("/fruits/", response_model=schemas.Fruit, status_code=201)
def create_fruit(fruit: schemas.FruitCreate, db: Session = Depends(get_db)):
    db_fruit = models.Fruit(**fruit.model_dump())
    db_fruit = models.FruitRepository(db).create_fruit(db_fruit)
    return schemas.FruitCreatedResponse(
        id=db_fruit.id,
        Status=schemas.Status.SUCCESS,
        name=db_fruit.name,
        description=db_fruit.description,
        flavor_variation=db_fruit.flavor_variation
    )

@app.get("/fruits", response_model=schemas.Fruit)
def read_fruits(db: Session = Depends(get_db)):
    fruits = models.FruitRepository(db).get_fruits()
    return schemas.GetFruitsResponse(
        Status=schemas.Status.SUCCESS,
        fruits=fruits
    )

@app.get("/fruits/{fruit_id}", response_model=schemas.Fruit)
def read_fruit(fruit_id: int, db: Session = Depends(get_db)):
    
    # Use the repository to encapsulate the database operations
    db_fruit = models.FruitRepository(db).get_fruit(fruit_id)

    if db_fruit is None:
        raise HTTPException(status_code=404, detail="Fruit not found")

    return schemas.GetFruitResponse(
        Status=schemas.Status.SUCCESS,
        id=db_fruit.id,
        name=db_fruit.name,
        description=db_fruit.description,
        flavor_variation=db_fruit.flavor_variation
    )
