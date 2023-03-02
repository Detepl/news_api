from django.db import models

# Create your models here.
class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField("Заголовок", max_length=35)
    short_description = models.CharField("Краткое описание", max_length=100)
    full_decsriprion = models.TextField("Полное описание")
    creation_date = models.DateField(verbose_name="Дата создания", auto_now_add = True)
    deletion_date = models.DateField(verbose_name="Дата удаления", null=True,blank=True)

    def __str__(self):
        return self.title
        # return self.short_description
        # return self.full_decsriprion
        # return self.creation_date
        # return self.deletion_date


