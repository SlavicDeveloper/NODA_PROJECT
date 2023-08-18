# Generated by Django 4.2.4 on 2023-08-16 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0003_alter_notes_doc_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="notes",
            name="category_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("soc", "Социальные науки"),
                    ("gum", "Гуманитарные науки"),
                    ("est", "Естественные и точные науки"),
                    ("med", "Медицинские науки"),
                    ("tech", "Техника и технологии"),
                    ("sel-hoz", "Сельскохозяйственные науки"),
                ],
                default="no status selected",
                help_text="text_type",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="notes",
            name="node_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]