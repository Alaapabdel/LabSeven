# Generated by Django 4.1.2 on 2022-11-18 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab7', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Branch',
        ),
        migrations.RemoveField(
            model_name='user',
            name='cc',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='userID',
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
