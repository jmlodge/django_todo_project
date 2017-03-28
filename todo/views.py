from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TodoSerializer
from .models import Todo


class TodoView(APIView):

    serializer_class = TodoSerializer

    def get(self, request, pk=None):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

