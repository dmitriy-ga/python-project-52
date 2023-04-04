from django.urls import path
from task_manager.labels import views


urlpatterns = [
    path('', views.LabelsIndex.as_view(), name='labels_index'),

    path('create/', views.LabelsCreate.as_view(), name='labels_create'),

    path('<int:label_id>/update/',
         views.LabelsUpdate.as_view(), name='labels_update'),

    path('<int:label_id>/delete/',
         views.LabelsDelete.as_view(), name='labels_delete'),
]
