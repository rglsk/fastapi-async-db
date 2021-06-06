from pydantic import BaseModel, BaseConfig


class BaseSchema(BaseModel):
    class Config(BaseConfig):
        allow_population_by_field_name = True
        orm_mode = True
