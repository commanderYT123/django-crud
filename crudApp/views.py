from django.shortcuts import render, redirect, get_object_or_404
from .forms import PersonForm
from .models import Person


def index(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PersonForm()
    people = Person.objects.all()
    return render(
        request,
        "index.html",
        {
            "people": people,
        },
    )


def delete(request, id):
    person = get_object_or_404(Person, id=id)
    person.delete()
    return redirect("index")


def edit(request, id):
    person = get_object_or_404(Person, id=id)
    people = Person.objects.all()
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = PersonForm(instance=person)

    return render(
        request,
        "edit.html",
        {
            "person": person,
            "form": form,
            "people": people,
        },
    )
