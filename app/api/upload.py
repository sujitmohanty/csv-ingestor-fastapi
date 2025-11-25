from fastapi import APIRouter, UploadFile, File, BackgroundTasks, Depends
from starlette.requests import Request
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.ingest_service import ingest_csv_to_db
from app.core.templates import templates


router = APIRouter(tags=["upload"])


@router.post("/upload-csv-web")
async def upload_csv_web(
    request: Request,
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    import os, uuid, shutil

    UPLOAD_DIR = "uploads"
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    temp_name = f"{uuid.uuid4()}_{file.filename}"
    temp_path = f"{UPLOAD_DIR}/{temp_name}"

    # Save file
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Ingest asynchronously
    background_tasks.add_task(ingest_csv_to_db, temp_path, db)

    # Render upload page again WITH success message
    return templates.TemplateResponse(
        "upload.html",
        {
            "request": request,
            "uploaded": True,
            "message": "Upload complete! You can now view the data."
        }
    )
