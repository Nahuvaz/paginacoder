# Generated by Django 4.2.7 on 2023-12-17 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musiblog', '0004_categorias_post_categoria'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categorias',
            new_name='Categories',
        ),
        migrations.RemoveField(
            model_name='post',
            name='categoria',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='music', max_length=255),
        ),
    ]
