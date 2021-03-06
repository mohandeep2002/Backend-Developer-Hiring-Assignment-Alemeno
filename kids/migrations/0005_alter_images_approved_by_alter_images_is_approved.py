# Generated by Django 4.0.3 on 2022-03-13 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kids', '0004_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='approved_by',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='images',
            name='is_approved',
            field=models.BooleanField(blank=True),
        ),
    ]
