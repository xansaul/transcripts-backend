# Generated by Django 5.1.1 on 2024-09-13 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videosTxts', '0006_remove_txtfile_video_videotranscription_txt_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='videotranscription',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
