from django.shortcuts import render, redirect
from component.models import Application
from component.forms import ApplicationForm


def application_create(request, template_name='component/component_form.html'):
    form = ApplicationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('application_new')
    return render(request, template_name, {'form':form})