import datetime
from uuid import UUID

from app.models.base import BaseSchema


class ArticleBase(BaseSchema):
    title: str
    slug: str
    text: str


class ArticleIn(ArticleBase):
    created_at: datetime.datetime = datetime.datetime.now(tz=datetime.timezone.utc)


class ArticleOut(ArticleBase):
    id: UUID
    created_at: datetime.datetime
