from django.shortcuts import render
from django.views.generic import CreateView
from .models import Notes
from django.urls import reverse_lazy
from .forms import RegisterUserForm



def NotesPreview(request):
    lst_of_names = ["soc", "gum", "est", "med", "tech", "selhoz"]
    context = {}
    for el in lst_of_names:
        filtered_data = Notes.objects.filter(category_status__contains=f"{el}")
        context[f'{el}'] = filtered_data
    return render(request, "main/notes_preview.html", context=context)


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
