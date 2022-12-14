# Generated by Django 4.0.7 on 2022-09-27 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='town',
            field=models.CharField(blank=True, choices=[('ji1', '서울특별시'), ('ji5', '광주광역시'), ('ji12', '충청남도'), ('ji6', '대전광역시'), ('ji4', '인천광역시'), ('ji14', '전라남도'), ('ji7', '울산광역시'), ('ji2', '부산광역시'), ('ji9', '경기도'), ('ji17', '제주특별자치도'), ('ji10', '강원도'), ('ji15', '경상북도'), ('ji11', '충청북도'), ('ji16', '경상남도'), ('ji3', '대구광역시'), ('ji13', '전라북도'), ('ji8', '세종특별자치시')], max_length=30, null=True, verbose_name='동네'),
        ),
    ]
