from django.shortcuts import render
from registration.models import Profile
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

# Create your views here.

class ProfilesListView(ListView):
    model =  Profile
    template_name = 'Profiles/profile_list.html'
    paginate_by = 3



class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'Profiles/profile_detail.html'

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])
    
