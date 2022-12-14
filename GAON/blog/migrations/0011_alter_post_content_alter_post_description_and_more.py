# Generated by Django 4.0.7 on 2022-09-29 15:45

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('blog', '0010_alter_post_town'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, help_text='simple description text', max_length=100, verbose_name='부제목'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='#Tags#'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, verbose_name='제목'),
        ),
        migrations.AlterField(
            model_name='post',
            name='town',
            field=models.CharField(blank=True, choices=[('광주광역시', '광주광역시'), ('인천광역시', '인천광역시'), ('경상남도', '경상남도'), ('전라남도', '전라남도'), ('제주특별자치도', '제주특별자치도'), ('강원도', '강원도'), ('세종특별자치시', '세종특별자치시'), ('충청남도', '충청남도'), ('경기도', '경기도'), ('전라북도', '전라북도'), ('충청북도', '충청북도'), ('대전광역시', '대전광역시'), ('서울특별시', '서울특별시'), ('경상북도', '경상북도'), ('울산광역시', '울산광역시'), ('부산광역시', '부산광역시'), ('대구광역시', '대구광역시')], max_length=30, null=True, verbose_name='동네'),
        ),
    ]
