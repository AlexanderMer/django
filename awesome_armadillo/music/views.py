from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View
from .models import Album
from .forms import UserForm

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


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    def get(self, request):  # if it's a GET request, this method will be called
        """Displays a blank form for a user to register"""
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):  # if it's a POST request, this method will be called
        """Processes form data submitted by user"""
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User object if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    #  request.user -> use this to reference user
                    return redirect('music:index')
        return render(request, self.template_name,  {'form':form})
