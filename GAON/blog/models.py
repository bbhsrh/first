from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
# 모어마
class Post(models.Model):
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
    
    town = models.CharField('동네',max_length=30, choices=town_choices, null=True, blank=True)    

    title = models.CharField('제목', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias')
    description = models.CharField('부제목', max_length=100, blank=True, help_text='simple description text')
    content = models.TextField('내용')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
    tags = TaggableManager('#Tags#', blank=True)    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OWNER', blank=True, null=True)
    
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'
        ordering = ('-id',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))
    
    def get_previous(self):
        return self.get_previous_by_modify_dt()
    
    def get_next(self):
        return self.get_next_by_modify_dt()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)