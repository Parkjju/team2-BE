# Generated by Django 3.2.13 on 2022-05-30 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartscheduler', '0003_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
