# from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Users, Project, Task_TODO
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import StringRelatedField, PrimaryKeyRelatedField


class SimpleUserModelSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = 'first_name, last_name'


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class ProjectModelSerializer(ModelSerializer):
    users = UserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class TaskTODOModelSerializer(ModelSerializer):
    user = UserModelSerializer()

    class Meta:
        model = Task_TODO
        fields = '__all__'
