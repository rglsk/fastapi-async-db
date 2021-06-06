from sqlalchemy import Column, String, Table, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import metadata


Article = Table(
    "article",
    metadata,
    Column(
        "id",
        UUID(),
        primary_key=True,
    ),
    Column("title", String(65)),
    Column("slug", String(65), nullable=False, unique=True),
    Column("text", Text),
    Column("created_at", DateTime(timezone=True)),
)
