# Generated by Django 5.1.1 on 2024-09-10 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recruitment',
            fields=[
                ('rec_id', models.AutoField(primary_key=True, serialize=False)),
                ('recruitment_possition', models.CharField(choices=[('Nothing', 'nothing'), ('Front End Developer', 'Front end Developer'), ('Back End Developer', 'back end developer'), ('Full Stack Developer', 'full stack developer'), ('DevOps Engineer', 'devOps engineer'), ('UX/UI Designer', 'UX/UI designer'), ('Network Engineer', 'network engineer')], default='Nothing', max_length=50)),
                ('recieved_resume', models.PositiveIntegerField()),
                ('checked_resume', models.PositiveIntegerField()),
                ('approved_resume', models.PositiveIntegerField()),
                ('interviewed_resume', models.PositiveSmallIntegerField()),
                ('time_spent_interview', models.DurationField()),
                ('recruitment_condition', models.CharField(choices=[('Accept', 'accepted'), ('Reject', 'reject'), ('Uncertain', 'uncertain')], default='Uncertain', max_length=50)),
                ('date_recruitment', models.DateField()),
            ],
        ),
    ]