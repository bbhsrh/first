from django.db import models
from django.urls import reverse

from photo.fields import ThumbnailImageField

# Create your models here.
class Region1(models.Model):
    town_choices = {
        ( '서울특별시','서울특별시'),
        ( '부산광역시','부산광역시'),
        ( '대구광역시','대구광역시'),
        ( '인천광역시','인천광역시'),
        ( '광주광역시','광주광역시'),
        ( '대전광역시','대전광역시'),
        ( '울산광역시','울산광역시'),
        ( '세종특별자치시','세종특별자치시'),
        ( '경기도','경기도'),
        ( '강원도','강원도'),
        ( '충청북도','충청북도'),
        ( '충청남도','충청남도'),
        ( '전라북도','전라북도'),
        ( '전라남도','전라남도'),
        ( '경상북도','경상북도'),
        ( '경상남도','경상남도'),
        ( '제주특별자치도','제주특별자치도')    
    }
    region1 = models.CharField('지역',max_length=30, choices=town_choices, null=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="OWNER", blank=True, null=True)

    def __str__(self):
        return self.region1
  
class Region2(models.Model):
    region1 = models.ForeignKey(Region1, on_delete = models.CASCADE, blank=True, verbose_name="지역",null=True)
    region2 = models.CharField('동네',max_length=30, null=True)    
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="OWNER", blank=True, null=True)

    def __str__(self):
        return self.region2
    
    def get_absolute_url(self):
        return reverse('photo:region_list', args=(self.id,))


class Region(models.Model):
    region2code = models.PositiveIntegerField(unique=True)
    region1code = models.PositiveIntegerField(blank=True)
    region1 = models.CharField(max_length=100, blank=True)
    region2 = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.region1name + " " + self.region2name

    def region1_region2(self):
        return {'region1':self.region1name, 'region2name':self.region2name}
    

class Photo(models.Model):
    region1 = models.ForeignKey(Region1, on_delete = models.CASCADE, blank=True, verbose_name="지역",null=True)
    region2 = models.ForeignKey(Region2, on_delete = models.CASCADE, blank=True, verbose_name="동네",null=True)
    title = models.CharField('상품제목', max_length=30, blank=True)
    description = models.TextField('상품 설명', blank=True)    
    price = models.IntegerField('상품 가격', blank=True, null=True)
    image = ThumbnailImageField(upload_to='photo/%Y/%m', blank=True)
    upload_dt = models.DateTimeField('Upload Date', auto_now_add=True, blank=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="판매자", blank=True, null=True)
        
    class Meta:
        ordering = ('-upload_dt',)
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=(self.id,))
