from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Indira Arifia Rahmah',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
