# Generated by Django 4.2 on 2023-04-08 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('letsmeet', '0003_locations'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkup',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='letsmeet.locations'),
            preserve_default=False,
        ),
    ]
