# Generated by Django 4.2.3 on 2023-07-28 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("erwandjango", "0004_people_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="people",
            name="city",
            field=models.CharField(default=1, max_length=30),
        ),
        migrations.AddField(
            model_name="people",
            name="country",
            field=models.CharField(default=1, max_length=30),
        ),
    ]
