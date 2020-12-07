from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from django.views import View
from django.views import generic

class Todo_main(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'todo_main/index.html'
        return render(request, template_name)


#Todo_main에는 TemplateView(일반적인 view)를 보여주는데 get 방시으로 받았을 떄는
#todo_main/index.html로 이동한다는 뜻