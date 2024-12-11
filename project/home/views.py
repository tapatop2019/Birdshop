
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .forms import AddPostForm

def sing(request): #request используется например для получения данный через метод get, post
    #t = render_to_string("project/project/templates/sing.html")# тоже обрабатывает шаблон, но отдельно в отличии от функции render
    #return HttpResponse(t) #HttpResponse отвечает за формирование ответа, соответствующего запросу и обратно клиенту.
    
    if request.method=="POST":

        form = AddPostForm(request.POST, request.FILES)# создаем экземляр AddPostForm()
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form=AddPostForm()
    data={'form': form} # и теперьб все атрибуты класса AddPostForm(),будут передоваться в ниже написаный context
    return render(request,"sing_page/sing.html",context=data) # функция render обрабатывает шаблон, третьий параметр позволяет передать из фунrции представления данные в указаный шаблон


# Если что-то непонятно смотреть #44 урок django ВЕСЬ