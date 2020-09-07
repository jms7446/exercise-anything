from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=11)


class User2(User):
    name2 = models.CharField(max_length=11)


class Person(models.Model):
    name = models.CharField(max_length=11)

    def __repr__(self):
        return f'<Person(name={self.name})>'

