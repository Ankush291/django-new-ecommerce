# Generated by Django 5.1.4 on 2025-01-06 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_category_categories'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
    ]