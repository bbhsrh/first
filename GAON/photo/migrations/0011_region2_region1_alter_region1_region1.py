# Generated by Django 4.0.7 on 2022-09-27 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0010_region1_region2_alter_photo_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='region2',
            name='region1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photo.region1', verbose_name='지역'),
        ),
        migrations.AlterField(
            model_name='region1',
            name='region1',
            field=models.CharField(choices=[('광주광역시', '광주광역시'), ('전라남도', '전라남도'), ('경기도', '경기도'), ('서울특별시', '서울특별시'), ('인천광역시', '인천광역시'), ('충청북도', '충청북도'), ('전라북도', '전라북도'), ('세종특별자치시', '세종특별자치시'), ('경상남도', '경상남도'), ('부산광역시', '부산광역시'), ('충청남도', '충청남도'), ('울산광역시', '울산광역시'), ('제주특별자치도', '제주특별자치도'), ('강원도', '강원도'), ('대구광역시', '대구광역시'), ('경상북도', '경상북도'), ('대전광역시', '대전광역시')], max_length=30, null=True, verbose_name='지역'),
        ),
    ]
