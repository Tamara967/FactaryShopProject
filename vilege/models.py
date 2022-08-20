from django.db import models



class Vilege(models.Model):
    vilege_name = models.CharField(max_length=150)

    def my_func(self):
        return "Hello my model"

    def __str__(self):
        return self.vilege_name

    class Meta:
        verbose_name = 'vilege'
