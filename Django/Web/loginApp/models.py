from django.db import models

# Create your models here.


class Signup(models.Model):
    user_email = models.CharField(max_length=200)
    user_pwd   = models.CharField(max_length=50)
    user_name  = models.CharField(max_length=50)

    def __str__(self):  # localhost:8000/admin에서 나타날문자
        return self.user_name

    class Meta:
        db_table = 'user_db'