# Generated by Django 5.1.1 on 2024-09-10 11:03

import personnal.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnal', '0002_alter_personnal_number_of_personnal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personnal',
            old_name='level_fo_position',
            new_name='level_for_position',
        ),
        migrations.AlterField(
            model_name='personnal',
            name='number_of_personnal',
            field=models.CharField(blank=True, db_index=True, default=personnal.models.Personnal.create_new_number_of_personnal, editable=False, max_length=100, unique=True),
        ),
    ]
