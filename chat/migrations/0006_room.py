# Generated by Django 3.2.9 on 2021-11-29 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_alter_message_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=100)),
                ('messages', models.ManyToManyField(blank=True, to='chat.Message')),
            ],
        ),
    ]