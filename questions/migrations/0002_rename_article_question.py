# Generated by Django 5.0.3 on 2024-03-20 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='Question',
        ),
    ]
