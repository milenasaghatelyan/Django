from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import *

# Create your views here.
class HomeListView(ListView):
    template_name='index.html'

    def get(self,request):
        contact= Contact.objects.get()
        socialmedia=SocialMedia.objects.get()
        generalslideractive=GeneralSliderActive.objects.all()
        generalslider=GeneralSlider.objects.all()
        features_items=Features_Items.objects.all()

        return render(request,self.template_name,{
                                'contact':contact,
                                'socialmedia':socialmedia,
                                'generalslideractive':generalslideractive,
                                'generalslider':generalslider,
                                'features_items':features_items,

                                     })