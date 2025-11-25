import os
import pandas as pd
from sqlalchemy.orm import Session
from app.models.dataset_row import DatasetRow

def ingest_csv_to_db(file_path: str, db: Session):
    total = 0

    # Read in chunks to avoid memory issues
    for chunk in pd.read_csv(file_path, chunksize=2000):
        records = chunk.to_dict(orient="records")
        objects = [DatasetRow(**row) for row in records]

        db.add_all(objects)
        db.commit()

        total += len(objects)

    os.remove(file_path)
    print(f"Ingested {total} rows.")
