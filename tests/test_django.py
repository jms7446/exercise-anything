import os
import django
from django.db import transaction
import pytest

# cur_dir = os.path.dirname(__file__)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.django_settings")
django.setup()


from db.models import User, Person


@transaction.atomic
def show_data():
    datas = User.objects.all()
    for data in datas:
        print(data)


def test_1(db):
    u = Person.objects.create(name='bb')
    u.save()
    print(Person.objects.all())


# if __name__ == '__main__':
    # Person.objects.create(name='aa')
    # print(Person.objects.all()[0].name)
    # pass
