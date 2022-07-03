from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from ast import Delete
from calendar import firstweekday
from multiprocessing import context
from operator import le
import re
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import *
from django.views import generic



class SignUpView(generic.CreateView):
    template_name='registration/signup.html'
    form_class=CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')


class LandingPageView(generic.TemplateView):
    template_name = 'landing_page.html'

def landing_page(request):
    return render(request,'landing_page.html')

class LeadListView(generic.ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = 'leads'

class LeadDetailView(generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = 'lead'

class LeadCreateView(generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')

    def form_valid(self, form):
        send_mail(
            subject="A lead has been created", 
            message="Go to site to see the lead",
            from_email='test@test.com',
            recipient_list=['test2@test.com']
        )
        return super(LeadCreateView,self).form_valid(form)

class LeadUpdateView(generic.UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')

class LeadDeleteView(generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead-list')
