# Generated by Django 4.1.7 on 2023-03-12 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_authors'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('-created',)},
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='publisher',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='published',
            new_name='created',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='authors',
        ),
    ]