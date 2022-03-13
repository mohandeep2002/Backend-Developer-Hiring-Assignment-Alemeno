from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class Kid(models.Model):
    kid_id = models.AutoField(primary_key=True)
    kid_name = models.CharField(max_length=30)
    kid_age = models.IntegerField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    parents_email_id = models.EmailField()
