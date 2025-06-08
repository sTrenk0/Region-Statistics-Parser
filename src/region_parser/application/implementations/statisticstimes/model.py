from region_parser.infrastructure.db.model import BaseModel
from tortoise import fields


class StatisticsTimesModel(BaseModel):
    subregion = fields.CharField(max_length=256, null=True)

    class Meta:
        table = "statisticstimes"
