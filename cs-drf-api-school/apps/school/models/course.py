from django.db import models
from django.utils.translation import gettext as _


class Course(models.Model):

    class Level(models.TextChoices):
        BASIC = 'BASIC', _('Basic')
        INTERMEDIARY = 'INTERMEDIARY', _('Intermediary')
        ADVANCED = 'ADVANCED', _('advanced')

    code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    level = models.CharField(choices=Level.choices, max_length=12, blank=False, null=False)


    class Meta:
        db_table = 'course'
        ordering = ['id']
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')

    def __str__(self) -> str:
        return self.description
