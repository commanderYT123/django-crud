from django.db import models


# Create your models here.
class Person(models.Model):
    username = models.CharField(
        max_length=50, null=True, verbose_name="username", db_column="username"
    )
    phone = models.CharField(
        max_length=11, null=True, verbose_name="phone", db_column="phone"
    )
    email = models.EmailField(
        max_length=254, null=True, verbose_name="email", db_column="email"
    )

    class Meta:
        db_table = "Persons"

    def __str__(self):
        return self.username
