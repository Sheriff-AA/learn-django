# Generated by Django 4.2 on 2023-04-08 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letsmeet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkup',
            name='image',
            field=models.ImageField(default='test', upload_to='images'),
            preserve_default=False,
        ),
    ]
