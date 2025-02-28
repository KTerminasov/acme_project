from django.shortcuts import render
from .forms import BirthdayForm


def birthday(request):
    form = BirthdayForm(request.GET or None)
    context = {'form': form}
    return render(request, 'birthday/birthday.html', context=context)