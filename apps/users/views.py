from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView


# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        group = Group.objects.get(name='guest')
        self.object = form.save()
        user = User.objects.get(username=self.object)
        group.user_set.add(user)
        return super().form_valid(form)


class UserListView(ListView):
    model = User
    template_name = 'registration/user-list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_role'] = self.request.user.groups.all()[0].name
        return context


class ChangeUserGroupView(View):
    def get(self, request, pk):
        groups = Group.objects.all()
        user = User.objects.get(pk=pk)

        context = {
            'groups': groups,
            'user': user
        }

        return render(request, 'registration/group-change.html', context)

    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        group_id = request.POST.get('group')

        group = Group.objects.get(pk=group_id)
        user.groups.set([group])

        return redirect('users:user-list')
