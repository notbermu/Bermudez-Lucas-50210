# Generated by Django 5.0.3 on 2024-03-25 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FootballApp', '0005_tourn_alter_league_division_alter_team_division'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tourn',
            old_name='numero_de_equipos',
            new_name='equipos',
        ),
    ]
