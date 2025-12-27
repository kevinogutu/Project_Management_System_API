from rest_framework import serializers
from .models import Project
from tasks.serializers import TaskSerializer 

class ProjectSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField(read_only=True)
    manager = serializers.PrimaryKeyRelatedField(queryset=... , required=False)  

    class Meta:
        model = Project
        fields = ['id','title','description','status','manager','tasks','created_at','updated_at']

    def get_tasks(self, obj):
        return TaskSerializer(obj.tasks.all(), many=True).data
