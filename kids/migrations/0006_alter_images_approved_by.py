# Generated by Django 4.0.3 on 2022-03-13 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kids', '0005_alter_images_approved_by_alter_images_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='approved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]