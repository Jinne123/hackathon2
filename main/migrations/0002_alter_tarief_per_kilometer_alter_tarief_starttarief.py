# Generated by Django 4.1.1 on 2022-10-06 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tarief", name="per_kilometer", field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="tarief", name="starttarief", field=models.IntegerField(),
        ),
    ]