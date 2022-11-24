
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        context = {}
        context['form'] = self.form_class(request.POST, request.FILES)
        return self.render_to_response(context)