from django.shortcuts import render
from . import models
from django.views.generic import  CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

def home_page(request):
    hospitals = models.Hospital.objects.all()
    context = {
        'hospitals': hospitals
    }
    return render(request, 'my_app/home_page.html', context)

def detail_page(request, pk):
    hospital = models.Hospital.objects.filter(id=pk).first()
    context = {
        'hospital': hospital
    }
    return render(request, 'my_app/detail_page.html', context)


class CreateHospital(LoginRequiredMixin, CreateView):
    model = models.Hospital
    fields = ['title', 'location']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class UpdateHospital(LoginRequiredMixin,  UserPassesTestMixin, UpdateView):
    model = models.Hospital
    fields = ['title', 'location']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        hospital = self.get_object()
        if hospital.owner == self.request.user:
            return True
        else:
            return False


class DeleteHospital(LoginRequiredMixin,  UserPassesTestMixin, DeleteView):
    model = models.Hospital
    success_url = '/'
    context_object_name = 'hospital'

    def test_func(self):
        hospital = self.get_object()
        if hospital.owner == self.request.user:
            return True
        else:
            return False

