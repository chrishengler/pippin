# Generated by Django 5.1.6 on 2025-03-31 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scambaiting', '0007_alter_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='baiter',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='email',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='email',
            name='cc',
            field=models.ManyToManyField(blank=True, to='scambaiting.person'),
        ),
    ]
