from django.shortcuts import render
from . import models, forms
from django.shortcuts import get_object_or_404

from django.http import Http404

def get_shows_all(request):
    shows = models.TVShow.objects.all()
    return render(request, "shows_list.html", {"shows": shows})


def get_show_detail(request, id):
    try:
        show = get_object_or_404(models.TVShow, id=id)
        try:
            comment = models.ShowComment.objects.filter(shows_id=id).order_by("created_date")
        except models.TVShow.DoesNotExist:
            print('No comments')
    except models.TVShow.DoesNotExist:
        raise Http404('TVSHOW does not exist, try another id')
    return render(request, "shows_detail.html", {"show": show, 'shows_comment': comment})


def add_show(request):
    method = request.method
    if method == "Post":
        form = forms.TVShowForm(request.POST. request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Show Created Successfully")
    else: