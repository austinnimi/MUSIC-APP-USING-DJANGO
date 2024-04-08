# Generated by Django 5.0.2 on 2024-04-07 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=50)),
                ('audio_file', models.FileField(upload_to='songs/')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='song_covers/')),
            ],
        ),
    ]
