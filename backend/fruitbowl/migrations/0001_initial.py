# Generated by Django 3.0.6 on 2020-05-24 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FruitBowl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fruit', models.CharField(max_length=120)),
                ('url', models.CharField(max_length=250)),
                ('visable', models.BooleanField(default=False)),
            ],
        ),
    ]