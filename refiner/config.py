from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional

class Settings(BaseSettings):
    """Global settings configuration using environment variables"""

    INPUT_DIR: str = Field(
        default="/input",
        description="Directory containing input files to process"
    )

    OUTPUT_DIR: str = Field(
        default="/output",
        description="Directory where output files will be written"
    )

    REFINEMENT_ENCRYPTION_KEY: str = Field(
        default=None,
        description="Key to symmetrically encrypt the refinement. This is derived from the original file encryption key"
    )

    SCHEMA_NAME: str = Field(
        default="Telegram Chats",
        description="Name of the schema"
    )

    SCHEMA_VERSION: str = Field(
        default="0.0.1",
        description="Version of the schema"
    )

    SCHEMA_DESCRIPTION: str = Field(
        default="Schema for dFusion Social Truth DLP Telegram chats",
        description="Description of the schema"
    )

    SCHEMA_DIALECT: str = Field(
        default="sqlite",
        description="Dialect of the schema"
    )

    # Optional, required if using https://pinata.cloud (IPFS pinning service)
    # PINATA_API_KEY: Optional[str] = Field(
    #     default=None,
    #     description="Pinata API key"
    # )

    # PINATA_API_SECRET: Optional[str] = Field(
    #     default=None,
    #     description="Pinata API secret"
    # )

    PINATA_API_JWT: Optional[str] = Field(
        default="",
        description="Pinata API JWT"
    )

    IPFS_GATEWAY_URL: str = Field(
        default="https://gateway.pinata.cloud/ipfs",
        description="IPFS gateway URL for accessing uploaded files"
    )

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()