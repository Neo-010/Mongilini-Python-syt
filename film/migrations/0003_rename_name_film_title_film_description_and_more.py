# Generated by Django 5.1.4 on 2025-01-05 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0002_film_image_alter_film_cinematographer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='film',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='films/'),
        ),
        migrations.AlterField(
            model_name='film',
            name='year',
            field=models.DateField(blank=True, null=True),
        ),
    ]
