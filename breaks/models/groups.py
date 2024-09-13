from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):
    organization = models.ForeignKey(
        'breaks.Organization', on_delete=models.RESTRICT, related_name='groups', verbose_name='Organization')
    name = models.CharField('Name', max_length=255)
    manager = models.ForeignKey(User, on_delete=models.RESTRICT,
                                related_name='group_managers', verbose_name='Manager',)
    employees = models.ManyToManyField(User, related_name='group_employees', verbose_name='Employees', blank=True)
    min_active = models.PositiveSmallIntegerField('Min active employees', null=True, blank=True,)
    break_start = models.TimeField('Break start', null=True, blank=True,)
    break_end = models.TimeField('Break end', null=True, blank=True,)
    break_max_duration = models.PositiveSmallIntegerField('Break max duration', null=True, blank=True,)

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} {self.pk}'
