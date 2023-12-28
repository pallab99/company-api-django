from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import Http404
from base.responseMessage import RESPONSE_MESSAGE
from .models import Company
from .serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response(
            {"message": RESPONSE_MESSAGE["get_all_data_success"],
                "data": response.data},
            status=status.HTTP_200_OK
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            {"success": True,
                "message": RESPONSE_MESSAGE["get_single_data_success"], "data": serializer.data},
            status=status.HTTP_200_OK
        )

    def create(self, request, *args, **kwargs):
        name = request.data.get("name")
        company_exists = Company.objects.filter(name=name).exists()
        if (company_exists):
            return Response(
                {"success": False, "message": "Duplicate company", }, status=status.HTTP_409_CONFLICT
            )
        response = super().create(request, *args, **kwargs)
        return Response(
            {"message": "Company created successfully",
                "data": response.data, }, status=status.HTTP_201_CREATED
        )

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(
            {"message": "Company updated successfully",
                "data": response.data, "status": response.status_code},
        )

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return Response(
            {"message": "Company deleted successfully",
                "status": response.status_code},
        )
