from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView, DetailView
from .forms import CustomUserCreationForm, LoginForm


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        context = {}
        context['form'] = form
        return self.render_to_response(context)

class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('index')
        else:
            form = LoginForm(request.POST)
        return self.render_to_response(context={'form':form})


def logout_view(request):
    logout(request)
    return redirect('index')


class ProfileView(DetailView):
    model = get_user_model()
    template_name = 'profile_detail.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        posts = self.object.posts.order_by('-created_at')
        kwargs['posts'] = posts
        return super().get_context_data(**kwargs)
