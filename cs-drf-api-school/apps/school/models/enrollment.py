from django.db import models
from django.utils.translation import gettext as _

from apps.school.models import Student, Course


class Enrollment(models.Model):

    class Period(models.TextChoices):
        MORNING = 'MORNING', _('Morning')
        AFTERNOON = 'AFTERNOON', _('afternoon')
        NIGHT = 'NIGHT', _('night')

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    period = models.CharField(choices=Period.choices, max_length=12, blank=False, null=False)


    class Meta:
        db_table = 'enrollment'
        ordering = ['id']
        verbose_name = _('Enrollment')
        verbose_name_plural = _('Enrollments')

    def __str__(self) -> str:
        return f'{self.course}-{self.student}-{self.period}'
