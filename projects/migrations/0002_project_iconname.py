# Generated by Django 5.1.7 on 2025-04-02 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='iconName',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
