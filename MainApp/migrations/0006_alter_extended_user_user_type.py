# Generated by Django 4.0.6 on 2022-12-04 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_alter_assignment_assign_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extended_user',
            name='user_type',
            field=models.CharField(choices=[('1', 'Admin'), ('2', 'Staff'), ('3', 'Student')], max_length=1),
        ),
    ]
