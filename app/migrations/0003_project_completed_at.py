# Generated by Django 4.2.11 on 2024-04-04 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_orfer_skill_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='completed_at',
            field=models.DateField(null=True),
        ),
    ]
