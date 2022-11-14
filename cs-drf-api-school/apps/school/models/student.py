from django.db import models
from django.utils.translation import gettext as _


class Student(models.Model):
    name = models.CharField(max_length=30)
    rg = models.CharField(unique=True ,max_length=9)
    cpf = models.CharField(unique=True, max_length=11)
    birth_date = models.DateField()
    phone = models.CharField(max_length=11, default="")


    class Meta:
        db_table = 'student'
        ordering = ['id']
        verbose_name = _('Student')
        verbose_name_plural = _('Students')

    def __str__(self) -> str:
        return self.name
