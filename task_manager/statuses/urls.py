from django.urls import path
from task_manager.statuses import views


urlpatterns = [
    path('', views.StatusesIndex.as_view(), name='statuses_index'),

    path('create/', views.StatusesCreate.as_view(), name='statuses_create'),

    path('<int:status_id>/update/',
         views.StatusesUpdate.as_view(), name='statuses_update'),

    path('<int:status_id>/delete/',
         views.StatusesDelete.as_view(), name='statuses_delete'),
]
