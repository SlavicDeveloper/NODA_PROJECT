from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Notes
from django.urls import reverse_lazy
from .forms import RegisterUserForm, ToValidateNotesForm
from django.contrib.auth.decorators import login_required



def NotesPreview(request):
    lst_of_names = ["soc", "gum", "est", "med", "tech", "selhoz"]

    context = {}
    for el in lst_of_names:
        filtered_data = Notes.objects.filter(category_status__contains=f"{el}")
        context[f'{el}'] = filtered_data
    return render(request, "main/notes_preview.html", context=context)


def index(request):
    return render(request, 'main/index.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


# class ToValidateNotes(CreateView):
#     model = Notes
#     form_class = ToValidateNotesForm
#     success_url = reverse_lazy('notes')
#     template_name = 'main/validate_notes.html'

@login_required
def ToValidateNotes(request):
    error = ''
    if request.method == "POST":
        form = ToValidateNotesForm(request.POST, request.FILES)
        if form.is_valid():
            noda = form.save(commit=False)
            noda.node_id = request.user
            if not form.data["doc_name"]:
                error = "Поле 'Название документа' обязательно к заполнению"
            else:
                form.save()
                return redirect("home")
    else:
        form = ToValidateNotesForm()

    return render(request, 'main/validate_notes.html', {'form': form, "error": error})