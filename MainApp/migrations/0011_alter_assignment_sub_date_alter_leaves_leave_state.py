# Generated by Django 4.1.4 on 2022-12-06 19:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0010_assignment_answer_alter_attendance_attendance_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='sub_date',
            field=models.DateField(default=datetime.date(2022, 12, 7)),
        ),
        migrations.AlterField(
            model_name='leaves',
            name='leave_state',
            field=models.CharField(choices=[('applied', 'Applied'), ('approved', 'Approved'), ('rejected', 'Rejected')], max_length=50),
        ),
    ]