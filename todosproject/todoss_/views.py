from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from .models import Users, Project, Task_TODO
# from .serex import UserSerializer
from .serializers import UserModelSerializer, ProjectModelSerializer, TaskTODOModelSerializer
from .ex import MUser


class UserModelViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class TaskTODOModelViewSet(ModelViewSet):
    queryset = Task_TODO.objects.all()
    serializer_class = TaskTODOModelSerializer
