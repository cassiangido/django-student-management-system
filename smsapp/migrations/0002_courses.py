# Generated by Django 5.1.7 on 2025-04-24 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coarsename', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('fees', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
