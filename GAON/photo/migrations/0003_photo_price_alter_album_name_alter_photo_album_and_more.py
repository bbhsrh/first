# Generated by Django 4.0.7 on 2022-09-26 17:12

from django.db import migrations, models
import django.db.models.deletion
import photo.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_album_owner_photo_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='photo.album'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=photo.fields.ThumbnailImageField(blank=True, upload_to='photo/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(blank=True, max_length=30, verbose_name='TITLE'),
        ),
    ]
