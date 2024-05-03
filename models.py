from datetime import datetime

from peewee import PostgresqlDatabase, Model, CharField, TextField, DateTimeField

from settings import postgre


db = PostgresqlDatabase(**postgre)


class Task(Model):
    title = CharField()
    describe = TextField(null=True)
    created_date = DateTimeField(default=datetime.now())

    def __str__(self):
        return f'Задание с заголовком: {self.title} и описанием {self.describe}'

    class Meta:
        database = db


db.create_tables([Task])

