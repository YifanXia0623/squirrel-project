# Generated by Django 3.1.2 on 2020-10-22 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0003_auto_20201022_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='Age',
            field=models.CharField(choices=[('Juvenile', 'Juvenile'), ('Adult', 'Adult')], default='Adult', help_text='Age of Squirrel', max_length=15),
        ),
    ]
