from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
from django.contrib.auth.models import User

class ClientViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Client.objects.all()
        serializer = ClientSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise NotFound("Client not found")
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise NotFound("Client not found")
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise NotFound("Client not found")
        serializer = ClientSerializer(client, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise NotFound("Client not found")
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProjectViewSet(viewsets.ViewSet):
    def create(self, request, client_pk=None):
        try:
            client = Client.objects.get(pk=client_pk)
        except Client.DoesNotExist:
            raise NotFound("Client not found")

        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(client=client, created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, client_pk=None):
        try:
            client = Client.objects.get(pk=client_pk)
        except Client.DoesNotExist:
            raise NotFound("Client not found")
        projects = client.project_set.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def retrieve(self, request, client_pk=None, pk=None):
        try:
            client = Client.objects.get(pk=client_pk)
            project = client.project_set.get(pk=pk)
        except (Client.DoesNotExist, Project.DoesNotExist):
            raise NotFound("Project not found")
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def update(self, request, client_pk=None, pk=None):
        try:
            client = Client.objects.get(pk=client_pk)
            project = client.project_set.get(pk=pk)
        except (Client.DoesNotExist, Project.DoesNotExist):
            raise NotFound("Project not found")
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, client_pk=None, pk=None):
        try:
            client = Client.objects.get(pk=client_pk)
            project = client.project_set.get(pk=pk)
        except (Client.DoesNotExist, Project.DoesNotExist):
            raise NotFound("Project not found")
        serializer = ProjectSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, client_pk=None, pk=None):
        try:
            client = Client.objects.get(pk=client_pk)
            project = client.project_set.get(pk=pk)
        except (Client.DoesNotExist, Project.DoesNotExist):
            raise NotFound("Project not found")
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
