# Generated by Django 4.1.7 on 2023-02-20 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35, verbose_name='Заголовок')),
                ('short_description', models.CharField(max_length=100, verbose_name='Краткое описание')),
                ('full_decsriprion', models.TextField(verbose_name='Полное описание')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('deletion_date', models.DateField(blank=True, null=True, verbose_name='Дата удаления')),
            ],
        ),
    ]