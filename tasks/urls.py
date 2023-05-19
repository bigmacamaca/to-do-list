from django.contrib import admin
from django.urls import path
from tasks import apis

app_name = "tasks"

urlpatterns = [
    path('api/create_task/', apis.TaskViewSet.as_view({'post':'create_task'})),
    path('api/get_tasks/', apis.TaskViewSet.as_view({'get':'get_tasks'})),
    path('api/search_task/', apis.TaskViewSet.as_view({'get':'search_task'})),
    path('api/get_task_details/<int:task_id>/', apis.TaskViewSet.as_view({'get':'get_task_details'})),
    path('api/update_task/<int:task_id>/', apis.TaskViewSet.as_view({'put':'update_task'})),
    path('api/delete_task/<int:task_id>/', apis.TaskViewSet.as_view({'delete':'delete_task'})),
    path('api/delete_all_tasks/', apis.TaskViewSet.as_view({'delete':'delete_all_tasks'})),    
]
