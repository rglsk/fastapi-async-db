import abc
import uuid
from typing import List, Mapping, Union, Dict

import databases
import sqlalchemy

from app.db.base import database
from app.models.articles import BaseSchema


class BaseRepository(abc.ABC):
    def __init__(self, db: databases.Database = database, *args, **kwargs) -> None:
        self._db = db
        super()

    @property
    @abc.abstractmethod
    def _table(self) -> sqlalchemy.Table:
        pass

    @property
    @abc.abstractmethod
    def _schema_out(self):
        pass

    @property
    @abc.abstractmethod
    def _schema_in(self):
        pass

    @staticmethod
    def generate_uuid() -> uuid.UUID:
        return uuid.uuid4()

    def _preprocess_create(self, values: Dict) -> Dict:
        if "id" not in values:
            values["id"] = self.generate_uuid()
        return values

    async def _list(self) -> List[Mapping]:
        query = self._table.select()
        return await self._db.fetch_all(query=query)

    async def list(self) -> List:
        rows = await self._list()
        return [self._schema_out(**dict(row.items())) for row in rows]

    async def create(self, values: Union[BaseSchema, Dict]) -> BaseSchema:
        if isinstance(values, dict):
            values = self._schema_in(**values)
        dict_values = self._preprocess_create(dict(values))

        query = self._table.insert()
        await self._db.execute(query=query, values=dict_values)
        return self._schema_out(**dict_values)
