# Generated by Django 2.2.1 on 2019-05-29 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190529_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='desc',
            field=models.TextField(blank=True, help_text='文章简介，字数保持在100以内！', max_length=100),
        ),
        migrations.AddField(
            model_name='article',
            name='read_nums',
            field=models.IntegerField(default=0, verbose_name='阅读量'),
        ),
    ]
