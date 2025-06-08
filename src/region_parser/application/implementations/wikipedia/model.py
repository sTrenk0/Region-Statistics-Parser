from region_parser.infrastructure.db.model import BaseModel
from tortoise import fields


class WikipediaModel(BaseModel):
    population = fields.IntField(null=True)

    class Meta:
        table = "wikipedia"
