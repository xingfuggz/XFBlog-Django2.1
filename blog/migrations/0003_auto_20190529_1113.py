# Generated by Django 2.2.1 on 2019-05-29 03:13

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190525_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=mdeditor.fields.MDTextField(),
        ),
    ]
