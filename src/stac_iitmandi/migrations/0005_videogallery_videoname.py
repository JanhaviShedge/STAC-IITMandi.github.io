# Generated by Django 3.1.2 on 2021-01-02 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stac_iitmandi', '0004_auto_20210102_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='videogallery',
            name='videoname',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
    ]
