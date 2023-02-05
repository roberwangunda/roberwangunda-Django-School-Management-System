from django.contrib.messages.views import SuccessMessageMixin
from django.forms import widgets
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import (HttpResponseRedirect, get_object_or_404,redirect, render)


import requests
from .models import Staff


class StaffListView(ListView):
    model = Staff


class StaffDetailView(DetailView):
    model = Staff
    template_name = "staffs/staff_detail.html"


class StaffCreateView(SuccessMessageMixin, CreateView):
    model = Staff
    fields = "__all__"
    # print(fields)
    # total_staffs = Staff.objects.all().count()
    success_message = "New staff successfully added"
    def get_form(self):
        """add date picker in forms"""
        form = super(StaffCreateView, self).get_form()
        form.fields["date_of_birth"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["date_of_admission"].widget = widgets.DateInput(
            attrs={"type": "date"}
        )
        form.fields["address"].widget = widgets.Textarea(attrs={"rows": 1})
        form.fields["others"].widget = widgets.Textarea(attrs={"rows": 1})

        return form
    

class StaffUpdateView(SuccessMessageMixin, UpdateView):
    model = Staff
    fields = "__all__"
    success_message = "Record successfully updated."

    def get_form(self):
        """add date picker in forms"""
        form = super(StaffUpdateView, self).get_form()
        form.fields["date_of_birth"].widget = widgets.DateInput(attrs={"type": "date"})
        form.fields["date_of_admission"].widget = widgets.DateInput(
            attrs={"type": "date"}
        )
        form.fields["address"].widget = widgets.Textarea(attrs={"rows": 1})
        form.fields["others"].widget = widgets.Textarea(attrs={"rows": 1})
        return form
        


class StaffDeleteView(DeleteView):
    model = Staff
    success_url = reverse_lazy("staff-list")

# def itaff(request):
#     staff = get_object_or_404(Staff)
#     staffs = Staff.objects.filter(staff=staff).count()
#     print(staffs)

#     return render(request,'main-app/index.html',{})

# class TotalStaffView(StaffListView):
#     model = Staff
#     template_name = "templates/index.html"

#     def get_total_staff(request):
#         total_staffs = Staff.objects.all().count()
#         context = {
#             'total_staffs': total_staffs
#         }
#         print(total_staffs)
#         return render(request,'templates/index.html', context)