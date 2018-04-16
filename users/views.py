from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.contrib.auth import get_user_model

# get extended User model
User = get_user_model()


class UserList(ListView):
    template_name = 'users_templates/user_list.html'
    model = User


class UserDetail(DetailView):
    template_name = 'users_templates/user_detail.html'
    model = User


class UserCreate(CreateView):
    template_name = 'users_templates/user_create.html'
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'birthday']


class UserRemove(DeleteView):
    model = User
    success_url = reverse_lazy('users:user-list')


class UserUpdate(UpdateView):
    model = User
    template_name = 'users_templates/user_edit.html'
    fields = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'birthday')


import csv

from django.http import HttpResponse


def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'Birthday', 'Email address', 'Random Number'])

    users = User.objects.all().values_list('username', 'birthday', 'email', 'random_number')
    for user in users:
        writer.writerow(user)

    return response
