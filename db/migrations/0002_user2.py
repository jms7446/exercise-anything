# Generated by Django 2.2.3 on 2019-07-09 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User2',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='db.User')),
                ('name2', models.CharField(max_length=11)),
            ],
            bases=('db.user',),
        ),
    ]
