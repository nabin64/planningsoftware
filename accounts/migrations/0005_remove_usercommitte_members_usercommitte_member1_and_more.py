# Generated by Django 5.0 on 2024-01-25 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_delete_contigencyrate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercommitte',
            name='members',
        ),
        migrations.AddField(
            model_name='usercommitte',
            name='member1',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usercommitte',
            name='member2',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usercommitte',
            name='member3',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usercommitte',
            name='member4',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
