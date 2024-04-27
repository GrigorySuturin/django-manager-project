from django.db import models


class ManagerItem(models.Model):
    title = models.CharField(max_length=250)
    done = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = '-id',
        verbose_name = 'Manager Item'
