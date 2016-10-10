from orm import Model,StringField,IntegerField

class User(Model):
    _table_='users'

    id = IntegerField(primary_key=True)
    name = StringField()