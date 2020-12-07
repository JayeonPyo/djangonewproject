

# Create your views here.


# Create your views here.
from django.shortcuts import render, redirect
from . models import TodoList
from .forms import TodoForm
from django.views import View
from django.views import generic

class Todo_board(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'todo_board/todo_list.html'
        todo_list = TodoList.objects.all()

        return render(request, template_name, {"todo_list": todo_list})

#detailview를 이용해서 편하게 상세보기 페이지 만듦
#context_object_name은 object의 이름을 설정해주는 것. 그래서 template에서 저 이름을 가지고 접근하게 함
class Todo_board_detail(generic.DetailView):
    model = TodoList
    template_name = 'todo_board/todo_board_detail.html'
    context_object_name = 'todo_list'

class Todo_board_update(generic.UpdateView):
    model = TodoList
    fields = ('title', 'content', 'end_date')
    template_name = 'todo_board/todo_board_update.html'
    success_url = '/board/'

    def form_valid(self, form):
        form.save()
        return render(self.request, 'todo_board/todo_board_success.html', {"message": "일정을 업데이트 했습니다. "})


# 오브젝트를 받아와서 폼 클래스를 받아온 후 이것을 return 해줘야함
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

# todo_delete view
class Todo_board_delete(generic.DeleteView):
    model = TodoList
    success_url = '/board/'
    context_object_name = 'todo_list'

#일정 추가하는 함수
def check_post(request):
    template_name = 'todo_board/todo_board_success.html'
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.todo_save()
            message = "일정을 추가하였습니다."
            return render(request, template_name, {"message": message})
    else:
        template_name = 'todo_board/insert.html'
        form = TodoForm
        return render(request, template_name, {"form": form})

#Todo_main에는 TemplateView(일반적인 view)를 보여주는데 get 방시으로 받았을 떄는
#todo_main/index.html로 이동한다는 뜻