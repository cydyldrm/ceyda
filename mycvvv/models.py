from django.db import models


# Create your models here.

class AbstractModel(models.Model):
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


class Meta:
    abstract = True


class GeneralSetting(AbstractModel):
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

    def __str__(self):
        return f"General Setting: {self.name}"

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)


class ImageSetting(AbstractModel):
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
    file = models.FileField(
        default="",
        verbose_name="File",
        blank=True,
        help_text="",
        upload_to='images/',
    )

    def __str__(self):
        return f"Image Setting: {self.name}"

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ('name',)
