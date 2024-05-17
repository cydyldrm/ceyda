from django.db import models

# Create your models here.
class GeneralSetting(models.Model):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Name Test",
        help_text="This is variable of the setting."
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Description",
    )
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Parameter",

    )
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name="updated date",

    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name="created date",

    )
def __str__(self):
    return f"General Setting: {self.name}"
class Meta:
    verbose_name = 'General Setting'
    verbose_name_plural = 'General Settings'
    ordering = ('name', )