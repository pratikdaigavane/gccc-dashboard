# Generated by Django 3.1.1 on 2020-10-05 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranklist', '0004_college_stamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='stamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
