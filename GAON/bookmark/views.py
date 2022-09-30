from django.shortcuts import render

from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin
from bookmark.models import Bookmark #[주의]

# Create your views here.
class BookmarkLV(ListView):
    model = Bookmark
    
class BookmarkDV(DetailView):
    model = Bookmark
    
class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class BookmarkChangeLV(LoginRequiredMixin, ListView):
    template_name = 'bookmark/bookmark_change_list.html'
    
    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)
    
class BookmarkUpdateView(OwnerOnlyMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

class BookmarkDeleteView(OwnerOnlyMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')
    

def TopKeyLV(request):
    from bs4 import BeautifulSoup
    import requests


    req = requests.get('https://www.daangn.com/top_keywords') 
    soup = BeautifulSoup(req.text, 'html.parser')
    keywords = soup.select('#top-keywords-list li')
    keyword_arr = []
    for keyword in keywords :
        link = keyword.find('a').attrs['href']
        word = keyword.select_one('a .keyword-text').get_text()
        rank = keyword.select_one('a .rank').get_text().strip()
        keyword_object = {
            "link": link,
            "word" : word,
            "rank": rank
        }
        keyword_arr.append(keyword_object) 
    data = {"keyword_arr" : keyword_arr}
    return render(request, "bookmark/bookmark_list.html", data)