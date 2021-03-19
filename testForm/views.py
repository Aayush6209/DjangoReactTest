from django.shortcuts import render
from .models import User
from django.http import HttpResponse
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

# SuperUser
# user, kites@123


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == "GET":
        users = User.objects.all()
        # article is a query set so thats why we apply many=True
        serializer = UserSerializer(users, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

    elif request.method == "POST":
        # data = JSONParser().parse(request)
        # serializer = ArticleSerializer(data=data)
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return JsonResponse(serializer.data, status=201)

        # return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
@api_view(['GET', 'DELETE', 'PUT'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        # return HttpResponse(status=404)
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UserSerializer(user)
        # return JsonResponse(serializer.data)
        return Response(serializer.data)

    elif request.method == "PUT":
        # data = JSONParser().parse(request)
        # serializer = ArticleSerializer(article, data=data)
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data)
            return Response(serializer.data)
        # return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    elif request.method == "DELETE":
        user.delete()
        # return HttpResponse(status=204)
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
