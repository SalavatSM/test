from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class ReplacementStatus(models.Model):
    code = models.CharField('Code', max_length=16, primary_key=True)
    name = models.CharField('Name', max_length=32)
    sort = models.PositiveSmallIntegerField('Sort', null=True, blank=True)
    is_active = models.BooleanField('Activity', default=True)

    class Meta:
        verbose_name = 'Shift status'
        verbose_name_plural = 'Shifts status'
        ordering = ('sort',)

    def __str__(self):
        return f'{self.code} {self.name}'


class Replacement(models.Model):
    group = models.ForeignKey('breaks.Group', on_delete=models.CASCADE,
                              related_name='replacements',
                              verbose_name='Group')
    date = models.DateField('Date of replacement')
    break_start = models.TimeField('Break start')
    break_end = models.TimeField('Break end')
    break_max_duration = models.PositiveSmallIntegerField('Maximum break duration')

    class Meta:
        verbose_name = 'Shift'
        verbose_name_plural = 'Shifts'
        ordering = ('-date',)

    def __str__(self):
        return f'Shift №{self.pk} for {self.group}'


class ReplacementEmployee(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='replacements',
                              verbose_name='Employee')
    replacement = models.ForeignKey('breaks.Replacement', on_delete=models.CASCADE,
                              related_name='Shift')
    status = models.ForeignKey('breaks.ReplacementStatus', on_delete=models.RESTRICT,
                               related_name='replacement_employees',
                               verbose_name='Status')
    date = models.DateField('Date of replacement')
    break_start = models.TimeField('Break start')
    break_end = models.TimeField('Break end')
    break_max_duration = models.PositiveSmallIntegerField('Maximum break duration')

    class Meta:
        verbose_name = 'Shift - Employee'
        verbose_name_plural = 'Shifts - Employees'

    def __str__(self):
        return f'Shift {self.replacement} for {self.employee}'
