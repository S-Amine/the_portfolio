# Generated by Django 4.2.3 on 2023-07-16 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_socialmedia_remove_project_contribution_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='color',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
