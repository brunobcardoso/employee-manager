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


class Employee(models.Model):
    """
    Stores employees' information
    """
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, unique=True, blank=False)
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name='employees'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'
        ordering = ('name',)

    def __str__(self):
        return self.name
