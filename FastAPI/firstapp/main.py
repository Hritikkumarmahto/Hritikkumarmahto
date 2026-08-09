from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
import requests
import json


from database import SessionLocal, engine, Base
import models, schemas


Base.metadata.create_all(bind=engine)

app = FastAPI(description="This is My first FastAPI app")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {
            "status": "ok",
            "db": "connected ✅"
        }

    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"DB connection failed: {str(e)} ❌"
        )


@app.get("/")
def test():
    return {"Message": "Hello to FastAPI"}


@app.post("/create_staff")
def create_staff(
    staff: schemas.StaffCreate,
    db: Session = Depends(get_db)
):
    new_staff = models.Staff(
        emp_name=staff.emp_name,
        emp_age=staff.emp_age,
        emp_city=staff.emp_city
    )

    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)

    return new_staff


@app.get("/staff")
def get_all_staff(db: Session = Depends(get_db)):
    staff = db.query(models.Staff).all()

    return staff


@app.get("/staff/{staff_id}")
def get_staff(staff_id: int, db: Session = Depends(get_db)):
    staff = (
        db.query(models.Staff)
        .filter(models.Staff.id == staff_id)
        .first()
    )

    return staff

@app.post("/staff/bulk-upload")
def bulk_upload_staff(db:Session=Depends(get_db)):
    try:
        with open("staff.json","r") as f:
            staff_list=json.load(f)

    except Exception as e:
        raise HTTPException(status_code=400,detail=f"Error {str(e)}")

    created=[]

    for item in staff_list:
        new_staff=models.Staff(
            emp_name=item["emp_name"],
            emp_age=item["emp_age"],
            emp_city=item["emp_city"]
        )
        db.add(new_staff)
        created.append(new_staff)
    db.commit()
    for staff in created:
        db.refresh(staff)
    return {"inserted ":len(created),"staff":created}

@app.delete("/staff/{staff_id}")
def delete_staff(staff_id: int,db:Session=Depends(get_db)):
    staff=db.query(models.Staff).filter(models.Staff.id==staff_id).first()
    if not staff:
        raise HTTPException(status_code=404)
    db.delete(staff)
    db.commit()
    return {"message":f"staff with id{staff_id} has been deleted"}

@app.delete("/staff")
def delete_all_staff(db:Session=Depends(get_db)):
    staff=db.query(models.Staff).delete()

    db.delete(staff)
    db.commit()
    return {"message":f"All staff deleted."}

@app.put("/staff/{staff_id}",response_model=Staff)
def put_in_staff(staff_id:int,db:Session=Depends(get_db),updated_data=staff):
    staff=db.query(models.Staff).filter(models.Staff.id==staff_id).first()
    if not staff:
        raise HTTPException(status_code=404)
    else:
        updated_data=staff.
