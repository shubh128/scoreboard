# Generated by Django 2.2.2 on 2019-07-04 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20190703_0906'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='playerdetails',
            new_name='player',
        ),
        migrations.RemoveField(
            model_name='player',
            name='round_score',
        ),
        migrations.AlterField(
            model_name='playerround',
            name='round_number',
            field=models.IntegerField(default=0),
        ),
    ]
