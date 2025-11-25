# CSV Ingestor FastAPI 🚀

A full-stack FastAPI application that allows users to:

✔ Upload a large CSV dataset  
✔ Ingest it into a PostgreSQL database  
✔ View results in a beautiful, paginated UI  
✔ Stay on the upload page after uploading  
✔ Navigate manually to the data table when ready  
✔ Render pages with Jinja2 templates  
✔ Use Tailwind CSS for modern styling

This project is ideal for learning backend + frontend integration, data ingestion, and full-stack Python development.

---

## 📌 Features

### **Backend**

- FastAPI-based web application
- CSV upload handled via HTML `<form>` or API
- Background ingestion using pandas for large CSVs
- PostgreSQL database (Docker recommended)
- SQLAlchemy ORM models
- Simple NEXT-button pagination
- Jinja2 template rendering

### **Frontend**

- Clean upload UI with Tailwind CSS
- Loading spinner during upload
- Success message after upload
- “View Data” button only used after successful ingestion
- Responsive data table
- Simple pagination (Next → Next → Next)

---

## 🏗 Project Structure

app/
├── api/
│ └── upload.py # Upload endpoints (HTML + API)
├── core/
│ ├── database.py # DB connection + get_db
│ └── templates.py # Jinja environment
├── models/
│ └── dataset_row.py # SQLAlchemy table
├── services/
│ └── ingest_service.py # CSV ingestion logic
├── static/
│ └── css/style.css
├── templates/
│ ├── upload.html # Upload UI
│ └── rows.html # Data table UI (paginated)
└── main.py # App entry point

yaml
Copy code

---

## 🐳 Running the Database with Docker

The easiest way to run PostgreSQL is via Docker:

````bash
docker run --name kaggle_db \
  -e POSTGRES_USER=kaggle \
  -e POSTGRES_PASSWORD=kaggle \
  -e POSTGRES_DB=kaggle_data \
  -p 5432:5432 -d postgres:16
This creates a fully working PostgreSQL instance on:


```bash
uvicorn app.main:app --reload
Open in your browser:

👉 http://127.0.0.1:8000/


🛠 Technologies Used
Python 3.10+

FastAPI

SQLAlchemy ORM

PostgreSQL

Docker

Jinja2 Templates

Tailwind CSS (CDN)

Pandas (CSV ingestion)


❤️ Author
Created by Sujit Mohanty
````
