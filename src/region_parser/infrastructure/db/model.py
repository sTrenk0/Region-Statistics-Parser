from tortoise import fields, models


class BaseModel(models.Model):
    id = fields.IntField(primary_key=True)
    country_name = fields.CharField(max_length=256, unique=True)
    population = fields.IntField()
    region = fields.CharField(max_length=256)
    subregion = fields.CharField(max_length=256)

    class Meta:
        abstract = True
