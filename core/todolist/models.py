from django.db import models


class Item(models.Model):
    CHOISES = [
        ('new', 'Новая'),
        ('in_process', 'В процессе'),
        ('done', 'Сделано')
    ]

    name = models.TextField(max_length=200, null=False, blank=False, verbose_name='Наименование')
    status = models.CharField(max_length=13, choices=CHOISES, default='Новая', verbose_name='Статус')
    created_at = models.DateField(null=True, default=None, verbose_name='Время окончания')
    updated_at = models.DateField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return "{}. {}".format(self.pk, self.name, self.status, self.created_at)
