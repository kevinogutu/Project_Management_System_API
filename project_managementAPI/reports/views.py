from rest_framework.views import APIView
from rest_framework.response import Response
from projects.models import Project
from tasks.models import Task

class SummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {
            'projects_total': Project.objects.count(),
            'projects_complete': Project.objects.filter(status='complete').count(),
            'tasks_total': Task.objects.count(),
            'tasks_by_status': {
                'todo': Task.objects.filter(status='todo').count(),
                'in_progress': Task.objects.filter(status='in_progress').count(),
                'done': Task.objects.filter(status='done').count(),
            }
        }
        return Response(data)
