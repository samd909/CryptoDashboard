# Generated by Django 5.1.2 on 2024-11-26 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_match_max_bots_match_owner_alter_robot_owner'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='matches',
            unique_together={('match_id', 'bot_id')},
        ),
    ]
