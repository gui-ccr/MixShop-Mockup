from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    PROJECT_NAME: str = "Mix Shop API"
    DEBUG: bool = True
    HOST: str = "0.0.0.0"
    PORT: int = int(os.getenv("PORT", "8000"))
    
    TINY_API_URL: str = "https://api.tiny.com.br/api2"
    TINY_API_TOKEN: str = ""
    
    ALLOWED_ORIGINS: str = "http://localhost:3000,http://localhost:5173"
    
    class Config:
        env_file = ".env"
        case_sensitive = True
    
    @property
    def origins_list(self) -> List[str]:
        if self.ALLOWED_ORIGINS == "*":
            return ["*"]
        return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",")]


settings = Settings()