# Generated by Django 2.0.3 on 2018-04-10 01:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('playlist_manager', '0002_auto_20180320_2312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist_name', models.CharField(help_text='Enter a playlist name', max_length=200)),
                ('playlist_description', models.CharField(default='', help_text='Enter a discription for your playlist', max_length=1000)),
                ('collaborative_status', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='playlist', to=settings.AUTH_USER_MODEL)),
                ('songs', models.ManyToManyField(to='playlist_manager.Song')),
            ],
        ),
    ]
