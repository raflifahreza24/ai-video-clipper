"""Application configuration."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_name: str = "ai-video-clipper-backend"
    environment: str = "development"


settings = Settings()
