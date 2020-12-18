from django.shortcuts import render
from .models import *
from django.views.generic import *
from django.urls import reverse_lazy
# Create your views here.
class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name' , 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name' , 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
