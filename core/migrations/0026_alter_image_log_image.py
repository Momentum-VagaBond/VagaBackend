# Generated by Django 4.0.4 on 2022-05-03 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_remove_log_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='log_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='log', to='core.log'),
        ),
    ]