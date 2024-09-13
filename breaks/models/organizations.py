from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Organization(models.Model):
    name = models.CharField('Name', max_length=255)
    director = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='organization_directors',
                                 verbose_name='Director')
    employees = models.ManyToManyField(User, related_name='organization_employees', verbose_name='Employees', blank=True)

    class Meta:
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} {self.pk}'



