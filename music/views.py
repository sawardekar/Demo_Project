# from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse,Http404
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from music.models import Album, Song
from django.template import loader


def detail(request, album_id):
    return HttpResponse("<h2>Detail for album_id :" + str(album_id) + "</h2>")


def music_list(request, template_name='music/music_list.html'):
    album = Album.objects.all()
    data = {}
    data['all_music'] = album
    return render(request, template_name, data)
    # template =loader.get_template('music/music_list.html')
    # context={
    #     'all_music':album,
    # }
    # return HttpResponse(template.render(context,request))


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ['id', 'artist', 'album_title', 'genre', 'album_log', 'repeat_song', 'date', 'city', 'comment']


def album_list(request, template_name='music/album_list.html'):
    album = Album.objects.all()
    data = {}
    data['all_album'] = album
    return render(request, template_name, data)


def album_create(request, template_name='music/album_form.html'):
    form = AlbumForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('album_list')
    return render(request, template_name, {'form': form})


def album_update(request, pk, template_name='music/album_form.html'):
    try:
        album = Album.objects.get(pk=pk)
        # album = get_object_or_404(Album, pk=pk)
        form = AlbumForm(request.POST or None, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, template_name, {'form': form})


def album_delete(request, pk, template_name='music/album_confirm_delete.html'):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        song_ids = Song.objects.filter(pk=pk)
        for song_id in song_ids:
            song_id.is_active = False
            song_id.save()
        return redirect('album_list')
    return render(request, template_name, {'object': album})


class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ['album', 'is_active', 'file_type', 'size', 'song_title']


def song_list(request, template_name='music/song_list.html'):
    song = Song.objects.all()
    data = {}
    data['all_song'] = song
    return render(request, template_name, data)


def song_create(request, template_name='music/song_form.html'):
    form = SongForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('song_list')
    return render(request, template_name, {'form': form})


def song_update(request, pk, template_name='music/song_form.html'):
    song = get_object_or_404(Song, pk=pk)
    form = SongForm(request.POST or None, instance=song)
    if form.is_valid():
        form.save()
        return redirect('song_list')
    return render(request, template_name, {'form': form})


def song_delete(request, pk, template_name='music/song_confirm_delete.html'):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'POST':
        song.delete()
        return redirect('song_list')
    return render(request, template_name, {'object': song})
