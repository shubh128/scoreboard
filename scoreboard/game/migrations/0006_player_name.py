# Generated by Django 2.2.2 on 2019-07-04 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20190704_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='name',
            field=models.CharField(default='Anon', max_length=200),
        ),
    ]