# Generated by Django 2.0 on 2019-05-06 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_remove_userfeedbackmodel_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question_relation',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
