from typing import Type

import sqlalchemy

from app.db.repositories.base import BaseRepository
from app.db.tables import Article
from app.models.articles import ArticleOut, ArticleIn


class ArticleRepository(BaseRepository):
    @property
    def _table(self) -> sqlalchemy.Table:
        return Article

    @property
    def _schema_out(self) -> Type[ArticleOut]:
        return ArticleOut

    @property
    def _schema_in(self) -> Type[ArticleIn]:
        return ArticleIn
