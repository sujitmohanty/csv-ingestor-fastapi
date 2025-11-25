from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request

# Database
from app.core.database import Base, engine, get_db

# Templates
from app.core.templates import templates

# Routers
from app.api.upload import router as upload_router

# ORM / SQL
from sqlalchemy.orm import Session
from sqlalchemy import select, func
from app.models.dataset_row import DatasetRow

# Create tables automatically
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# API router (for /api/upload-csv, etc.)
app.include_router(upload_router, prefix="/api")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})


@app.get("/rows")
def get_rows(
    request: Request,
    page: int = 1,
    page_size: int = 50,
    db: Session = Depends(get_db),
):
    if page < 1:
        page = 1

    # Count total rows
    total_rows = db.scalar(select(func.count()).select_from(DatasetRow)) or 0

    offset = (page - 1) * page_size
    rows = (
        db.execute(
            select(DatasetRow)
            .offset(offset)
            .limit(page_size)
        )
        .scalars()
        .all()
    )

    # Convert ORM objects to plain dicts for Jinja
    rows_dict = [row.__dict__.copy() for row in rows]
    for r in rows_dict:
        r.pop("_sa_instance_state", None)

    # Determine if there's a next page
    has_next = offset + page_size < total_rows

    return templates.TemplateResponse(
        "rows.html",
        {
            "request": request,
            "rows": rows_dict,
            "page": page,
            "page_size": page_size,
            "has_next": has_next,
        },
    )
