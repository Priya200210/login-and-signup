# Generated by Django 4.1.3 on 2024-07-22 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_pages_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_detials',
            old_name='student',
            new_name='student_name',
        ),
    ]
