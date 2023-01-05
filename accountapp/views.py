from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.models import HelloWorld

from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from articleapp.models import Article


# Create your views here.
def index(request):
    return HttpResponse("Hello, accountapp 직접 응답토록 내가 추가한 페이지.")

has_ownership = [
    login_required, account_ownership_required
]


@login_required
def hello_world(request):
    # return HttpResponse('Hello Pinerest Account app world!')
    # return render(request, 'accountapp/hello_world.html')
    if request.user.is_authenticated:
        if request.method == 'POST':
            get = request.POST.get('hello_world')
            new_hello_world = HelloWorld()
            new_hello_world.text = get
            new_hello_world.save()
            #return HttpResponseRedirect(reverse('accountapp:hello_world'))
            return render(request, 'accountapp/hello_world.html', context={'hello_world_list': HelloWorld.objects.all()})
            #return render(request, 'accountapp/hello_world.html', context={'text' : 'POST REQUEST'})
        else:
            return render(request, 'accountapp/hello_world.html', context={'text': 'GET REQUEST'})
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))

            #return render(request, 'accountapp/hello_world.html', context={'hello_world_list': HelloWorld.objects.all()})
            #return HttpResponseRedirect(reverse('accountapp:login'))

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 5

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseForbidden()


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseForbidden()
