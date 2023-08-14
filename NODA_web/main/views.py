from django.shortcuts import render
from django.views.generic import CreateView
from .models import Notes
from django.urls import reverse_lazy
from .forms import RegisterUserForm






def NotesPreview(request):
    docs = Notes.objects.all()
    return render(request, "main/notes_preview.html", context={'notes': docs})


def index(request):
    return render(request, 'main/index.html')


# def registration(request):
#     context = {}
#     context['form'] = RegisterUserForm()
#     return render(request, 'main/registration.html', context)

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))
