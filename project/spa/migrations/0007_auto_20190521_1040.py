# Generated by Django 2.2.1 on 2019-05-21 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0006_auto_20190521_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='color',
            field=models.CharField(default='#F7DC6F', max_length=8),
        ),
    ]
