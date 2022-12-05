# Generated by Django 4.0.6 on 2022-12-05 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0009_createassign_created_by_alter_assignment_assign'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='answer',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attendance_state',
            field=models.CharField(choices=[('1', 'Present'), ('0', 'Absent')], max_length=1),
        ),
    ]