# Generated by Django 4.0.4 on 2022-05-06 23:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_rename_contacts_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='log_image',
        ),
        migrations.AddField(
            model_name='image',
            name='log',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='core.log'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='log',
            name='location',
            field=models.CharField(max_length=75),
        ),
    ]
