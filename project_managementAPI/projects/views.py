from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer
from .permissions import IsProjectManagerOrReadOnly, IsProjectManager
from rest_framework.permissions import IsAuthenticated
from tasks.serializers import TaskSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated & IsProjectManagerOrReadOnly]

    # Custom action to change status
    @action(detail=True, methods=['patch'], url_path='status', permission_classes=[IsAuthenticated, IsProjectManager])
    def change_status(self, request, pk=None):
        project = self.get_object()
        status_value = request.data.get('status')
        if status_value not in dict(Project.STATUS_CHOICES):
            return Response({'detail':'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)
        
        project.status = status_value
        project.save()
        serializer = self.get_serializer(project)
        return Response(serializer.data)

    # Custom action to get or create tasks for a project
    @action(detail=True, methods=['get','post'], url_path='tasks')
    def project_tasks(self, request, pk=None):
        project = self.get_object()
        if request.method == 'GET':
            serializer = TaskSerializer(project.tasks.all(), many=True)
            return Response(serializer.data)
        else:  # POST - create task under project
            data = request.data.copy()
            data['project'] = project.id
            serializer = TaskSerializer(data=data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)