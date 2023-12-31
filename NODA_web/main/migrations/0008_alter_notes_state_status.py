# Generated by Django 4.2.4 on 2023-08-18 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_notes_state_status_delete_tovalidatenotes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notes",
            name="state_status",
            field=models.CharField(
                blank=True,
                choices=[("approve", "Проверенно"), ("disapprove", "Не проверено")],
                default="disapprove",
                help_text="text_type",
                max_length=255,
            ),
        ),
    ]
