# Generated by Django 4.0.3 on 2022-03-14 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0006_alter_images_approved_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='updated_on',
            field=models.DateField(blank=True),
        ),
    ]
