# Generated by Django 4.0.7 on 2022-09-28 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0012_alter_region1_region1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region2code', models.PositiveIntegerField(unique=True)),
                ('region1code', models.PositiveIntegerField(blank=True)),
                ('region1name', models.CharField(blank=True, max_length=100)),
                ('region2name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='region1',
            name='region1',
            field=models.CharField(choices=[('제주특별자치도', '제주특별자치도'), ('인천광역시', '인천광역시'), ('강원도', '강원도'), ('대구광역시', '대구광역시'), ('경상남도', '경상남도'), ('충청남도', '충청남도'), ('서울특별시', '서울특별시'), ('경기도', '경기도'), ('경상북도', '경상북도'), ('울산광역시', '울산광역시'), ('세종특별자치시', '세종특별자치시'), ('충청북도', '충청북도'), ('전라남도', '전라남도'), ('전라북도', '전라북도'), ('대전광역시', '대전광역시'), ('부산광역시', '부산광역시'), ('광주광역시', '광주광역시')], max_length=30, null=True, verbose_name='지역'),
        ),
    ]
