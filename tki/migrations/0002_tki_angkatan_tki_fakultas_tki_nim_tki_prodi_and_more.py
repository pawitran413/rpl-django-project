# Generated by Django 5.1.1 on 2024-09-16 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tki',
            name='angkatan',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tki',
            name='fakultas',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tki',
            name='nim',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tki',
            name='prodi',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tki',
            name='status',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
