from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg://kaggle:kaggle@localhost:5432/kaggle_data"

settings = Settings()
