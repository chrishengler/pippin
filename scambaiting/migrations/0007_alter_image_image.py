# Generated by Django 5.1.6 on 2025-03-30 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scambaiting', '0006_alter_email_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
