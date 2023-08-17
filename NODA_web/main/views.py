from django.shortcuts import render
from django.views.generic import CreateView
from .models import Notes
from django.urls import reverse_lazy
from .forms import RegisterUserForm, ToValidateNotesForm



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


def ToValidateNotes(request):
    if request.method == 'GET':
        context = {'form' : ToValidateNotesForm()}
        return render(request, 'main/validate_notes.html', context)
    if request.method == "POST":
        notes = Notes(node_id=request.user)
        form = ToValidateNotesForm(data=request.POST, instance=notes)
        if form.is_valid():
            form.instance.node_id = request.user
            form.save()
            return render(request, 'main/suc.html')