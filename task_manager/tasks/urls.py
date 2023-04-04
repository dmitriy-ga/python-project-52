from django.urls import path
from task_manager.tasks import views


urlpatterns = [
    path('', views.TasksIndex.as_view(), name='tasks_index'),

    path('create/', views.TasksCreate.as_view(), name='tasks_create'),

    path('<int:task_id>/', views.TasksShow.as_view(), name='tasks_show'),

    path('<int:task_id>/update/',
         views.TasksUpdate.as_view(), name='tasks_update'),

    path('<int:task_id>/delete/',
         views.TasksDelete.as_view(), name='tasks_delete'),
]
