from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from todosproject.todoss.ex import MUser


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    email = serializers.CharField(max_length=128)


    #user = MUser('Кырф', 'kyrf.pda@gmail.com')
    #serializers = UserSerializer(user)
    #print(serializers.data)

    #render = JSONRenderer()
    #json_data = render.render(serializers.data)

    #print(json_data)