from django.shortcuts import render
from . import forms

# Create your views here.

def index(request):
    context_dict = {'text' : 'hello world!', 'number':100}
    return render(request, 'basicforms/index.html', context_dict)

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # Do something code
            print("Validation Success!")
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])

    return render(request, 'basicforms/form_page.html', {'form':form})
