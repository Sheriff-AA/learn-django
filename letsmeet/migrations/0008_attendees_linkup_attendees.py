# Generated by Django 4.2 on 2023-04-08 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letsmeet', '0007_rename_locations_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='linkup',
            name='attendees',
            field=models.ManyToManyField(blank=True, null=True, to='letsmeet.attendees'),
        ),
    ]