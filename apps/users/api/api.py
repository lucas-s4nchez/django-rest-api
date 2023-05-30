from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import MyUser
from apps.users.api.serializars import MyUserSerializer


@api_view(['GET', 'POST'])
def user_api_view(request):
    if request.method == 'GET':
        users = MyUser.objects.all()
        users_serializer = MyUserSerializer(users, many=True)
        return Response(users_serializer.data)

    if request.method == 'POST':
        users_serializer = MyUserSerializer(data=request.data)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response(users_serializer.data)
        return Response(users_serializer.errors)
