# Generated by Django 4.0.3 on 2022-03-13 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kid',
            name='kid_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
