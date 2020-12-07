from django import forms
from .models import TodoList


# django에서 form을 만들어주는 곳
#form.Modelfrom을 상속받고 class Meta 안에 model은 TodoList이고 필드는
#title, content, end_date를 작성한다
#ModelForm은 Meta class에게 의존하여 필드를 자동으로 생성해준다

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ('title', 'content', 'end_date')