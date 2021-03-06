# Generated by Django 4.0.3 on 2022-03-13 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kids', '0003_alter_kid_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField()),
                ('is_approved', models.BooleanField()),
                ('food_group', models.CharField(choices=[('Veg', 'Veg'), ('Fruit', 'Fruit'), ('Grain', 'Grain'), ('Protein', 'Grain'), ('Dairy', 'Dairy'), ('Confectionery', 'Confectionery'), ('Unknown', 'Unknown')], max_length=20)),
                ('approved_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('image_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kids.kid')),
            ],
        ),
    ]
