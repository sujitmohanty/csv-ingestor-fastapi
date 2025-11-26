# CSV Ingestor FastAPI 

A full-stack FastAPI application that allows users to:

✔ Upload a large CSV dataset (from Kaggle)
✔ Ingest it into a PostgreSQL database  
✔ View results in a beautiful, paginated UI  
✔ Stay on the upload page after uploading  
✔ Navigate manually to the data table when ready  
✔ Render pages with Jinja2 templates

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

- UI with Tailwind CSS
- Loading spinner during upload
- Success message after upload
- “View Data” button only used after successful ingestion
- Responsive data table
- Simple pagination

---
