# Generated by Django 4.2.4 on 2023-08-10 18:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_alter_user_id_notes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notes",
            name="doc_file",
            field=models.FileField(
                max_length=200,
                upload_to="uploads",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["doc", "docx"]
                    )
                ],
                verbose_name="docx_format_field",
            ),
        ),
    ]
