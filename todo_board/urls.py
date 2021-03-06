from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'todo_board'

urlpatterns = [
    url(r'^$', views.Todo_board.as_view(), name='todo_board'),
    url(r'^insert/$', views.check_post, name='todo_board_insert'),
    url(r'^(?P<pk>[0-9]+)/detail/$', views.Todo_board_detail.as_view(), name='todo_board_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.Todo_board_update.as_view(), name='todo_board_update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.Todo_board_delete.as_view(), name='todo_board_delete'),
    # url(r'^board/insert$', views.Todo_insert.as_view(), name='todo_board'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



#r'^(?P<pk>[0-9]+ >> pk는 게시판 고유 번호 즉 고유번호/detail url로 들어가면 해당 고유번호에 따른 게시판을 상세보기로 볼 수 있다