from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ...models import Todo
from ..serialiers import TodoSerializer

class TodoView(APIView):
    def get(self,request):
        todos = Todo.objects.order_by("-date")
        todoss = TodoSerializer(todos,many=True)
        return Response(todoss.data)
    
    def post (self,request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class DeleteTodoView(APIView):
    def delete(self,request,pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response({"message":"error while deleting"},status=status.HTTP_400_BAD_REQUEST)
        todo.delete()
        return Response({"message":"deleted succesfully"},status=status.HTTP_200_OK)
    
class UpdateTodoView(APIView):
    def put(self,request,pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response({"message":"error while updating"},status=status.HTTP_400_BAD_REQUEST)
        todo.checked=not todo.checked
        todo.save()
        serializer = TodoSerializer(todo,many=False)
        return Response({"message":serializer.data},status=status.HTTP_200_OK)
        
        