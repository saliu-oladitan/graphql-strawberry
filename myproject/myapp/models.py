from django.db import models
from django.forms import ModelForm

# Create your models here.


class UserModel(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("id",)


class UserForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ("first_name", "last_name")
