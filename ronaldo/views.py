from django.views import generic
from .models import Match, Links

class IndexView(generic.ListView):
    template_name = 'ronaldo/home.html'
    context_object_name = 'all_matches'

    def get_queryset(self):
        return Match.objects.all()


class DetailView(generic.DetailView):
    model = Match
    template_name = 'ronaldo/detail.html'
