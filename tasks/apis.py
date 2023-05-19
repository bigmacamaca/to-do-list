from tasks.models import Task
from tasks.serializers import TaskSerializer, UpdateTaskSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.http import JsonResponse

class TaskViewSet(viewsets.ViewSet):
    
    def get_tasks(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        if tasks:
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print("No tasks found!")
            return Response({"error": "No tasks found!"}, status=status.HTTP_400_BAD_REQUEST)
        
    def get_task_details(self, request, task_id, *args, **kwargs):
        task = Task.objects.get(id = task_id)

        if task:
            serializer = TaskSerializer(task)
            print("Retrieved Task with Task ID", task_id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Task does not exist!"},
                status = status.HTTP_400_BAD_REQUEST
            )
    
    def search_task(self, request, *args, **kwargs):
        title = request.query_params.get('title', None)

        if title is not None:
            taskQuery = Task.objects.filter(title__icontains=title)
        serializer = TaskSerializer(taskQuery, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def create_task(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update_task(self, request, task_id, *args, **kwargs):
        task = Task.objects.get(id=task_id)

        serializer = UpdateTaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete_task(self, request, task_id, *args, **kwargs):
        task_instance = Task.objects.get(id=task_id)

        if task_instance:
            task_instance.delete()
            print("Task Deleted!")
            return Response({"res": "Task Deleted!"}, status=status.HTTP_200_OK)
        else:
            print("Task not found!")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete_all_tasks(self, request, *args, **kwargs):
        task_instance = Task.objects.all()

        if task_instance:
            task_instance.delete()
            print("All tasks deleted!")
            return Response({"res": "All tasks deleted!"}, status=status.HTTP_200_OK)
        else:
            print("Task is already empty!")
            return Response(status=status.HTTP_400_BAD_REQUEST)
