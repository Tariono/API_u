from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
)
from .serializers import Key_wordSerializer, Key_wordDetailsSerializer
from .models import Key_word

# Create your views here.


class Key_wordViewSet(viewsets.ModelViewSet):
    queryset = Key_word.objects.all().order_by('-id')
    serializer_class = Key_wordSerializer


    @action(methods=['get'],detail=True)
    def videos(self, request, pk=id):
        key_word = self.get_object()
        serializer = Key_wordDetailsSerializer(key_word)
        return Response(serializer.data, status=200)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid username and/or password'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def signup(request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")
    user = User.objects.create_user(username, email, password)
    user = authenticate(username=username, password=password)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=HTTP_201_CREATED)
