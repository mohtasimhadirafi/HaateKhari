# Generated by Django 3.1.4 on 2021-02-08 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowYourself', '0002_auto_20210208_0541'),
    ]

    operations = [
        migrations.AddField(
            model_name='bodypartsdetection',
            name='action',
            field=models.CharField(default='frontalFace', max_length=10),
        ),
        migrations.AlterField(
            model_name='bodypartsdetection',
            name='image',
            field=models.ImageField(upload_to='images/result_dump'),
        ),
    ]
