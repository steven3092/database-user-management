from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ListOfUserSerializer
from .models import ListOfUser

from django.shortcuts import get_object_or_404

# class ListOfUserViewSet(viewsets.ModelViewSet):
#     queryset = ListOfUser.objects.all().order_by('name')
#     serializer_class = ListOfUserSerializer


class ListOfUserViews(APIView):
    def post(self, request):
        serializer = ListOfUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, id=None):
        if id:
            user = ListOfUser.objects.get(id=id)
            serializer = ListOfUserSerializer(user)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        users = ListOfUser.objects.all()
        serializer = ListOfUserSerializer(users, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    def patch(self, request, id=None):
        user = ListOfUser.objects.get(id=id)
        serializer = ListOfUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
    def delete(self, request, id=None):
        user = get_object_or_404(ListOfUser, id=id)
        user.delete()
        return Response({"status": "success", "data": "User Deleted"})