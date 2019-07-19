from django.db import models
from django.utils.encoding import force_text
from django.core.validators import validate_slug, validate_email, RegexValidator
import re

class users(models.Model) :
    alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabets are allowed.')
    username=models.CharField(max_length=30, validators=[alphanumeric], primary_key=True )
    user_id=models.IntegerField(unique=True)
    user_dob=models.DateField()
    