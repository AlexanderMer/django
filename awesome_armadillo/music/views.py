from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Album

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'albums'  # by default this variable is 'object_list'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album  # we're feeding pk from urls.py and parent class takes care of the rest for us
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album  # specifies which type of object to create. here we need album
    fields = ['artist', 'album_title', 'genre', 'album_logo',]


class AlbumUpdate(UpdateView):
    model = Album  # specifies which type of object to create. here we need album
    fields = ['artist', 'album_title', 'genre', 'album_logo',]


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')
