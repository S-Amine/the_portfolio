# Generated by Django 4.2.3 on 2023-07-16 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_testimonial_job_alter_skill_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='rate',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
