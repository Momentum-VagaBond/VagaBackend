# Generated by Django 4.0.4 on 2022-05-05 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_alter_trip_subscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='log_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='log', to='core.log'),
        ),
    ]
