from django.db import models


class Directory(models.Model):
    """ Модель справочника """
    name = models.CharField(
        verbose_name="Наименование",
        max_length=255,
        unique=True,
    )
    short_name = models.CharField(
        verbose_name="Короткое наименование",
        max_length=128,
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=False,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Справочник"
        verbose_name_plural = "Справочники"


class DirectoryVersion(models.Model):
    """ Модель версии справочника """
    directory = models.ForeignKey(
        "Directory",
        verbose_name="Справочник",
        on_delete=models.CASCADE,
        related_name="versions",
    )
    version = models.CharField(
        verbose_name="Версия",
        max_length=255,
    )
    start_date = models.DateField(
        verbose_name="Дата начала действия справочника этой версии",
    )

    def __str__(self):
        return f"{self.directory.name} : {self.version}"

    class Meta:
        verbose_name = "Версия справочника"
        verbose_name_plural = "Версии справочника"
        constraints = [
            # уникальная версия справочника
            models.UniqueConstraint(
                fields=("directory", "version"),
                name="unique_directory_version"
            ),
            # уникальная дата начала действия справочника
            models.UniqueConstraint(
                fields=("directory", "start_date"),
                name="unique_directory_start_date"
            )
        ]


class Item(models.Model):
    """ Модель элемента справочника """
    parent = models.ForeignKey(
        "self",
        verbose_name="Родительский идентификатор",
        on_delete=models.CASCADE,
        related_name="childs",
        null=True,
        blank=True,
    )
    code = models.CharField(
        verbose_name="Код элемента",
        max_length=256,
        null=False,
    )
    value = models.CharField(
        verbose_name="Значение элемента",
        max_length=256,
        null=False
    )
    directory_version = models.ForeignKey(
        "DirectoryVersion",
        verbose_name="Версия справочника",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.code} для \"{self.directory_version}\""

    def save(self, *args, **kwargs):
        # Если дочерняя версия не совпадает с версией каталога - падаем
        if self.parent:
            assert(self.parent.directory_version == self.directory_version)

        return super(Item, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Элемент справочника"
        verbose_name_plural = "Элементы справочника"

