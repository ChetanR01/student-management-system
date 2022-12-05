# Generated by Django 4.0.6 on 2022-12-04 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_alter_extended_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='assign_state',
            field=models.CharField(choices=[('submitted', 'Submitted'), ('notsubmitted', 'Not Submitted'), ('checked', 'Checked'), ('late', 'Delayed')], default='submitted', max_length=50),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attendance_state',
            field=models.CharField(choices=[('1', 'Present'), ('0', 'Absent')], default='1', max_length=1),
        ),
    ]
