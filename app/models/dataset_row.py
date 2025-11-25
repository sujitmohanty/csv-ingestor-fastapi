from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class DatasetRow(Base):
    __tablename__ = "dataset_rows"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    work_year: Mapped[int] = mapped_column(Integer, nullable=False)
    experience_level: Mapped[str] = mapped_column(String(10), nullable=False)
    employment_type: Mapped[str] = mapped_column(String(10), nullable=False)
    job_title: Mapped[str] = mapped_column(String(255), nullable=False)

    salary: Mapped[int] = mapped_column(Integer, nullable=False)
    salary_currency: Mapped[str] = mapped_column(String(10), nullable=False)
    salary_in_usd: Mapped[int] = mapped_column(Integer, nullable=False)

    employee_residence: Mapped[str] = mapped_column(String(10), nullable=False)
    remote_ratio: Mapped[int] = mapped_column(Integer, nullable=False)

    company_location: Mapped[str] = mapped_column(String(10), nullable=False)
    company_size: Mapped[str] = mapped_column(String(10), nullable=False)
