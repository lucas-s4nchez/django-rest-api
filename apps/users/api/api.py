from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.models import MyUser
from apps.users.api.serializars import MyUserSerializer, MyUserListSerializer


@api_view(['GET', 'POST'])
def users_api_view(request):
    if request.method == 'GET':
        users = MyUser.objects.all().values('id', 'email', 'username', 'password')
        users_serializer = MyUserListSerializer(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        users_serializer = MyUserSerializer(data=request.data)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response({'message': f"El usuario ha sido creado correctamente"}, status=status.HTTP_201_CREATED)
        return Response(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_api_view(request, id):
    user = MyUser.objects.filter(id=id).first()

    if user:
        if request.method == 'GET':
            user_serializer = MyUserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            # actualizar el usuario con la nueva data
            user_serializer = MyUserSerializer(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            # eliminar el usuario
            user.delete()
            return Response({'message': f"El usuario con el id '{id}' ha sido eliminado correctamente"}, status=status.HTTP_200_OK)

    return Response({'message': f"No existe el usuario con el id: {id}"}, status=status.HTTP_400_BAD_REQUEST)
