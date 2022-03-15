from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models import Choices


class Kid(models.Model):
    kid_id = models.AutoField(primary_key=True)
    kid_name = models.CharField(max_length=30)
    kid_age = models.IntegerField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    parents_email_id = models.EmailField()

    def __str__(self):
        return self.kid_name


class Images(models.Model):
    image_id = models.ForeignKey(Kid, on_delete=models.CASCADE)
    image_url = models.URLField()
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(blank=True, null=True)
    is_approved = models.BooleanField(blank=True)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    all_groups = (
        ('Veg', 'Veg'),
        ('Fruit', 'Fruit'),
        ('Grain', 'Grain'),
        ('Protein', 'Protein'),
        ('Dairy', 'Dairy'),
        ('Confectionery', 'Confectionery'),
        ('Unknown', 'Unknown')
    )
    food_group = models.CharField(choices=all_groups, max_length=20)
