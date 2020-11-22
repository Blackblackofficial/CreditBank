from django.shortcuts import render, redirect
from .forms import PersonForm
from .models import Person


# SiteView
def index(request):
    # persons = Person.objects.order_by('-name')  # А так же можно отсортировать полюбому другому полю, можно указать
    return render(request, 'bank/index.html',
                  {
                      'title': 'Главная страница',
                      # 'name': persons
                  })


def clients(request):
    return render(request, 'bank/clients.html')


def calculator(request):
    error = ''
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bank')
        else:
            error = 'Ошибка'

    form = PersonForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'bank/calculator.html', context)
