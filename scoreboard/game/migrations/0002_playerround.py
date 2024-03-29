# Generated by Django 2.2.2 on 2019-07-03 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerRound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', models.IntegerField(max_length=100)),
                ('score', models.IntegerField(max_length=25)),
                ('RoundPlayer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Player')),
            ],
        ),
    ]
