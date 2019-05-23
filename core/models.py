from django.db import models


class Department(models.Model):
    """
    Stores departments information
    """
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        verbose_name = 'department'
        verbose_name_plural = 'departments'

    def __str__(self):
        return self.name
