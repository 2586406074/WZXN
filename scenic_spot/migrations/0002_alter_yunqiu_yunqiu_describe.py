# Generated by Django 4.0.1 on 2022-05-09 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenic_spot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yunqiu',
            name='yunqiu_describe',
            field=models.CharField(max_length=1000),
        ),
    ]