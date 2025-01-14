
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('genres', models.CharField(max_length=255)),
                ('directed', models.CharField(max_length=255)),
                ('producers', models.CharField(max_length=255)),
                ('screenwriters', models.CharField(max_length=255)),
                ('cinematographer', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
