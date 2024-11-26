# Generated by Django 5.1.3 on 2024-11-23 23:07

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0003_alter_page_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="page",
            name="content",
            field=ckeditor_uploader.fields.RichTextUploadingField(
                verbose_name="Contenido"
            ),
        ),
        migrations.AlterField(
            model_name="page",
            name="created",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Fecha de Creación"
            ),
        ),
        migrations.AlterField(
            model_name="page",
            name="updated",
            field=models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición"),
        ),
    ]