from django.urls import path
from task_manager.users import views


urlpatterns = [
    path('', views.UsersIndex.as_view(), name='users_index'),

    path('create/', views.UsersCreate.as_view(), name='users_create'),

    path('<int:user_id>/update/',
         views.UsersUpdate.as_view(), name='users_update'),

    path('<int:user_id>/delete/',
         views.UsersDelete.as_view(), name='users_delete'),
]
