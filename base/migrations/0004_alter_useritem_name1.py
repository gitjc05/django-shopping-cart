# Generated by Django 4.1 on 2022-09-02 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_useritem_name_useritem_name1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useritem',
            name='name1',
            field=models.CharField(default='name', max_length=200),
        ),
    ]
