# Generated by Django 5.1.1 on 2024-09-30 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0005_rename_condition_profile_problemsinput'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='blood_pressure',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
        migrations.AddField(
            model_name='profile',
            name='diabetes',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
    ]
