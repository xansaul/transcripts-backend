# Generated by Django 5.1.1 on 2024-09-15 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videosTxts', '0007_videotranscription_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='videotranscription',
            name='url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
